import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="PlantDoc — Diagnostic Agricole",
    page_icon="🌿",
    layout="centered"
)

# Charger le modèle
@st.cache_resource
def charger_modele():
    return tf.keras.models.load_model('best_model.keras')

model = charger_modele()

# Catégories
categories = [
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

recommandations = {
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 'Appliquer un fongicide à base de strobilurine. Éviter l\'irrigation par aspersion.',
    'Corn_(maize)___Common_rust_': 'Utiliser des variétés résistantes. Appliquer un fongicide préventif.',
    'Corn_(maize)___Northern_Leaf_Blight': 'Retirer les feuilles infectées. Appliquer un fongicide systémique.',
    'Corn_(maize)___healthy': '✅ Plante saine. Continuer les bonnes pratiques agricoles.',
    'Orange___Haunglongbing_(Citrus_greening)': '⚠️ Maladie grave sans traitement curatif. Arracher et détruire les plants infectés.',
    'Pepper,_bell___Bacterial_spot': 'Appliquer un bactéricide à base de cuivre. Éviter de mouiller le feuillage.',
    'Pepper,_bell___healthy': '✅ Plante saine. Continuer les bonnes pratiques agricoles.',
    'Potato___Early_blight': 'Appliquer un fongicide préventif. Retirer les feuilles infectées.',
    'Potato___Late_blight': '⚠️ Traitement urgent avec fongicide. Détruire les plants très infectés.',
    'Potato___healthy': '✅ Plante saine. Continuer les bonnes pratiques agricoles.',
    'Tomato___Bacterial_spot': 'Appliquer un bactéricide à base de cuivre. Éviter l\'excès d\'humidité.',
    'Tomato___Early_blight': 'Appliquer un fongicide. Retirer les feuilles du bas infectées.',
    'Tomato___Late_blight': '⚠️ Traitement urgent. Appliquer un fongicide systémique immédiatement.',
    'Tomato___Leaf_Mold': 'Améliorer la ventilation. Appliquer un fongicide à base de soufre.',
    'Tomato___Septoria_leaf_spot': 'Retirer les feuilles infectées. Appliquer un fongicide préventif.',
    'Tomato___Spider_mites Two-spotted_spider_mite': 'Appliquer un acaricide. Augmenter l\'humidité autour des plants.',
    'Tomato___Target_Spot': 'Appliquer un fongicide. Éviter l\'excès d\'humidité foliaire.',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Pas de traitement curatif. Contrôler les aleurodes vecteurs.',
    'Tomato___Tomato_mosaic_virus': 'Pas de traitement curatif. Arracher et détruire les plants infectés.',
    'Tomato___healthy': '✅ Plante saine. Continuer les bonnes pratiques agricoles.'
}

# Interface
st.title("🌿 PlantDoc")
st.subheader("Diagnostic de maladies agricoles par IA")
st.write("Développé pour les agriculteurs d'Afrique centrale")

st.divider()

photo = st.file_uploader(
    "📸 Uploade une photo de feuille",
    type=['jpg', 'jpeg', 'png']
)

if photo is not None:
    img = Image.open(photo).convert('RGB')
    st.image(img, caption="Photo uploadée", width=300)

    with st.spinner("Analyse en cours..."):
        img_resized = img.resize((128, 128))
        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array, verbose=0)
        classe_index = np.argmax(predictions)
        confiance = float(np.max(predictions)) * 100
        classe = categories[classe_index]

        culture, maladie = classe.split('___')
        culture = culture.replace('_', ' ')
        maladie = maladie.replace('_', ' ')

    st.divider()

    if confiance >= 80:
        st.success(f"**Culture :** {culture}")
        st.error(f"**Maladie détectée :** {maladie}") if 'healthy' not in classe else st.success(f"**État :** {maladie}")
        st.metric("Confiance", f"{confiance:.1f}%")
    elif confiance >= 60:
        st.warning(f"**Culture :** {culture} — **{maladie}** (confiance moyenne : {confiance:.1f}%)")
    else:
        st.error(f"Confiance trop faible ({confiance:.1f}%). Essayez une photo plus nette.")

    st.divider()
    st.info(f"💊 **Recommandation :** {recommandations.get(classe, 'Consulter un agronome.')}")

st.divider()
st.caption("PlantDoc v1.0 — Périel Nitcheu — ENSPY Yaoundé, Cameroun")
