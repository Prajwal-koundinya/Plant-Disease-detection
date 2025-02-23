import os
import torch
import torchvision.transforms as transforms
import numpy as np
import cv2
from flask import Flask, request, render_template, jsonify
from PIL import Image
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image, preprocess_image
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

# Load the trained model
MODEL_PATH = "plant_disease_model.pth"  # Change this to your model's path
model = torch.load(MODEL_PATH, map_location=torch.device('cpu'))
model.eval()

# Define image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Flask app setup
app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define Grad-CAM function
def get_gradcam(image_tensor, model):
    target_layers = [model.layer4[-1]]  # Adjust for your model's architecture
    cam = GradCAM(model=model, target_layers=target_layers)
    targets = [ClassifierOutputTarget(0)]  # Change as needed
    grayscale_cam = cam(input_tensor=image_tensor, targets=targets)[0]
    return grayscale_cam

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"})
        file = request.files['file']
        if file.filename == "":
            return jsonify({"error": "No file selected"})
        
        img_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(img_path)
        
        # Load image
        image = Image.open(img_path).convert("RGB")
        input_tensor = transform(image).unsqueeze(0)
        
        # Model Prediction
        with torch.no_grad():
            output = model(input_tensor)
            predicted_class = torch.argmax(output).item()
        
        # Grad-CAM Visualization
        gradcam_mask = get_gradcam(input_tensor, model)
        img_array = np.array(image) / 255.0
        visualization = show_cam_on_image(img_array, gradcam_mask, use_rgb=True)
        vis_path = os.path.join(UPLOAD_FOLDER, "gradcam_" + file.filename)
        cv2.imwrite(vis_path, cv2.cvtColor(visualization, cv2.COLOR_RGB2BGR))
        
        return render_template("result.html", img_path=img_path, vis_path=vis_path, prediction=predicted_class)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
