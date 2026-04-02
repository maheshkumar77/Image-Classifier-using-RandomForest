from flask import Flask, render_template, request
import cv2
import numpy as np
import pickle
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Image Prediction
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    # Create uploads folder if not exists
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    # Secure filename
    from werkzeug.utils import secure_filename
    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    # Save file
    file.save(filepath)

    print("Saved file path:", filepath)

    # Check file exists
    if not os.path.exists(filepath):
        return "File was not saved correctly"

    # Check file size
    if os.path.getsize(filepath) == 0:
        return "Uploaded file is empty"

    print("File size:", os.path.getsize(filepath))

    # Read image
    img = cv2.imread(filepath)

    print("Image object:", img)

    if img is None:
        return "ERROR: OpenCV could not read the image"

    print("Image shape:", img.shape)

    # Safe resize
    img_resized = cv2.resize(img, (64, 64))

    img_flat = img_resized.flatten().reshape(1, -1)

    prediction = model.predict(img_flat)

    label = "Dog" if prediction[0] == 1 else "Cat"

    print("Prediction:", label)

    # Draw box
    h, w, _ = img.shape

    cv2.rectangle(
        img,
        (50, 50),
        (w - 50, h - 50),
        (255, 0, 0),
        3
    )

    cv2.putText(
        img,
        label,
        (60, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    result_filename = "result_" + filename

    result_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        result_filename
    )

    cv2.imwrite(result_path, img)

    return render_template(
        "index.html",
        result_image=result_filename,
        label=label
    )

if __name__ == "__main__":
    app.run(debug=True)