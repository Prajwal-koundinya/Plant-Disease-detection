# 🌿 Plant Disease Detection using AI & Grad-CAM 🔍

## 📌 Overview
This project leverages **Deep Learning (CNNs)** to detect plant diseases from images and provides **explainability** using **Grad-CAM (Gradient-weighted Class Activation Mapping)**. The model highlights the most important regions in an image contributing to the classification decision.

## 🚀 Features
✅ **AI-Powered Disease Detection** – Identifies plant diseases with high accuracy.  
✅ **Grad-CAM Explanation** – Visualizes important regions influencing the prediction.  
✅ **Flask Web App** – User-friendly web interface for disease detection.  
✅ **Easy to Deploy** – Run locally or on cloud platforms like AWS/GCP.  

## 🖼️ Demo
![image](https://github.com/user-attachments/assets/d0ddb082-4b90-448a-adbb-1d0501227992)
 
*Above: An example of a leaf image with Grad-cam highlighted disease regions.*

## 🛠️ Tech Stack
- **Python** 🐍
- **PyTorch** 🔥
- **Flask** 🌎
- **Grad-CAM** 🎯
- **OpenCV** 📷
- **Matplotlib & Seaborn** 📊

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
![App UI](https://user-images.githubusercontent.com/example-ui.png)

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

