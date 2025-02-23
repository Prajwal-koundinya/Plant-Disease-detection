# 🌿 Plant Disease Detection using AI & Grad-CAM 🔍

## 📌 Overview
This project leverages **Deep Learning (CNNs)** to detect plant diseases from images and provides **explainability** using **Grad-CAM (Gradient-weighted Class Activation Mapping)**. The model highlights the most important regions in an image contributing to the classification decision.

## 🚀 Features
✅ **AI-Powered Disease Detection** – Identifies plant diseases with high accuracy.  
✅ **Grad-CAM Explanation** – Visualizes important regions influencing the prediction.  
✅ **Flask Web App** – User-friendly web interface for disease detection.  
✅ **Easy to Deploy** – Run locally or on cloud platforms like AWS/GCP.  

## 🖼️ Demo Grad-cam
![image](https://github.com/user-attachments/assets/d0ddb082-4b90-448a-adbb-1d0501227992)
 
*Above: An example of a leaf image with Grad-cam highlighted disease regions.*

## ⚙️ **Technologies Used**

| **Technology**       | **Logo**                                                                                  |
|-----------------------|-------------------------------------------------------------------------------------------|
| **Python**           | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **PyTorch**          | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| **Flask**            | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) |
| **HTML**             | ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) |
| **CSS**              | ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |
| **JavaScript**       | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
| **Matplotlib**       | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white) |
| **GitHub**           | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) |


## 📂 Project Structure
```
📁 plant-disease-detection
│-- app.py                 # Flask application
│-- model.py               # AI model (CNN-based)
│-- static/
│   ├── uploads/           # Uploaded images
│   ├── results/           # Processed Grad-CAM images
│-- templates/
│   ├── index.html         # Main upload page
│   ├── result.html        # Prediction page
│-- requirements.txt       # Dependencies
│-- README.md              # Project documentation
```

## 🎯 How to Run
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/plant-disease-detection.git
cd plant-disease-detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```

### 4️⃣ Open in Browser
Visit `http://127.0.0.1:5000` in your web browser.

## 📌 Example Usage
1️⃣ Upload an image of a **plant leaf**.  
2️⃣ The model predicts the **disease category**.  
3️⃣ **Grad-CAM visualization** shows affected regions.  

## 🎨 UI Preview
![image](https://github.com/user-attachments/assets/3cc99126-01d2-49fb-8d23-9073f5d1daa8)


## 📊 Results
| Disease | Model Prediction | Confidence |
|---------|-----------------|------------|
| Bacterial Spot | ✅ Correct | 95.2% |
| Late Blight | ✅ Correct | 97.6% |

## 📖 Future Improvements
- [ ] Improve dataset diversity.
- [ ] Optimize model performance.
- [ ] Deploy on **Hugging Face** or **Streamlit Cloud**.

## 🤝 Contributing
Feel free to **fork** this repo and submit a **pull request**! 😊

## 📜 License
This project is licensed under the **MIT License**.

---
🔥 *If you like this project, don't forget to ⭐ it on GitHub!*

