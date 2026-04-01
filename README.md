# 🖼️ Image Classifier using Machine Learning

This project is a simple **image classification system** built using:

* Python 🐍
* OpenCV 📷
* NumPy 🔢
* Scikit-learn 🤖

It can classify images (e.g., Dog 🐶 or Cat 🐱) using a **Random Forest Classifier**.

---

## 🚀 Features

* Load image dataset from folders
* Preprocess images (resize + flatten)
* Train a machine learning model
* Predict class from:

  * Local image
  * Online image URL

---

## 📁 Dataset Structure

dataset/
├── cats/
├── dogs/

Each folder represents a class label.

---

## ⚙️ Installation

Install required libraries:

pip install numpy opencv-python scikit-learn matplotlib requests

---

## 🧠 How It Works

1. Read images using OpenCV
2. Resize images to 64x64
3. Flatten images into 1D arrays
4. Train model using RandomForestClassifier
5. Predict new images

---

## 🏃‍♂️ Run the Project

### Train Model

Run your training script:

python train.py

---

### Test with Image

You can test using:

* Local file
* Online image URL

Example:

url = "https://example.com/dog.jpg"

---

## 📊 Example Output

Predicted class: dog

---

## ⚠️ Limitations

* Works best on small datasets
* Not as accurate as deep learning models (CNN)

---

## 🔮 Future Improvements

* Use CNN (TensorFlow / PyTorch)
* Add GUI or Web App
* Improve accuracy with more data

---

## 👨‍💻 Author

Mahesh Kumar Sahu

---

## ⭐ Contribute

Feel free to fork this repo and improve it!
