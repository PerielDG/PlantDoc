# 🌿 PlantDoc — AI Plant Disease Detection

AI-powered plant disease detection system designed for farmers in Central Africa.

**Live Demo:** https://plantdoc-8dpfvtstemacancsyyndaj.streamlit.app/

---

## 🎯 Problem

Crop diseases destroy harvests across Cameroon and Central Africa every year. 
Farmers lack access to fast, affordable diagnostic tools. PlantDoc aims to 
provide instant disease diagnosis from a simple leaf photo.

## 🌱 Supported Crops

- 🌽 Corn (Maize) — 4 conditions
- 🍅 Tomato — 10 conditions  
- 🥔 Potato — 3 conditions
- 🍊 Orange — 1 condition
- 🫑 Pepper — 2 conditions

## 🤖 Technology

- **Model:** MobileNetV2 (Transfer Learning)
- **Dataset:** PlantVillage — 32,146 images, 20 classes
- **Accuracy:** 80.86% on test data
- **Framework:** TensorFlow, Streamlit
- **Deployment:** Streamlit Cloud

## ⚠️ Known Limitations

- Model shows bias toward Orange and Tomato classes due to class imbalance 
  in training data (5,507 orange images vs 513 corn images)
- Trained on 128x128 images — higher resolution would improve accuracy
- Dataset does not include local Cameroonian crops (cassava, plantain, 
  macabo) — future versions will integrate locally collected data

## 🔮 Future Work

- Collect local leaf photos from Yaoundé to build a Cameroonian dataset
- Re-train with balanced classes and 224x224 resolution
- Add GPS-based disease mapping (Folium)
- Add drone aerial image analysis

## 👨‍💻 Author

**DJAMBOU NITCHEU Gérard Périel** — Engineering Student, ENSPY Yaoundé, Cameroon  
*"Science au service de l'homme"*

## 📄 License

MIT License
