# 😄 Emotion Detection Web App

This is a full-stack Emotion Detection web app that uses a **Convolutional Neural Network (CNN)** to detect facial expressions in real-time using your webcam. The project includes:

- 🧠 A trained deep learning model (Keras `.h5` file)
- 🎥 A backend in **Flask** for video streaming and inference
- ⚛️ A frontend in **React** with a webcam toggle interface
- 🌐 Connected using **RESTful API + OpenCV**

---

## 🧱 Project Structure

```
emotion_detection/
├── backend/              # Flask app with Keras model and OpenCV
│   ├── app.py            # Main backend server
│   ├── best_model.h5     # Pre-trained CNN model
│   ├── templates/        # HTML for testing (optional)
│
├── frontend/             # React frontend
│   ├── src/              # React components and webcam toggle UI
│   ├── public/
│   ├── package.json
│
├── .gitignore
├── README.md
```

---

## 🚀 How to Run This Project

### ⚙️ Backend (Flask + Keras)

1. Create a virtual environment and install dependencies:
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate     # On Windows
   pip install -r requirements.txt
   ```

2. Run the backend server:
   ```bash
   python app.py
   ```

   This starts the Flask server at `http://localhost:5000`

---

### 💻 Frontend (React)

1. Install dependencies and run the app:
   ```bash
   cd frontend
   npm install
   npm start
   ```

2. Open the browser at:  
   `http://localhost:3000`

> The frontend fetches live video from the backend, and shows detected emotions with a toggle button to start/stop the webcam.

---

## 🧠 AI/ML Model Details

### 📊 Dataset: FER-2013

- 48x48 grayscale facial images
- 7 Emotion Classes: `Angry`, `Disgust`, `Fear`, `Happy`, `Sad`, `Surprise`, `Neutral`
- Preprocessing: grayscale → resize → normalize → reshape

### 🏗️ CNN Architecture

- 4 convolutional blocks with BatchNorm, MaxPool, Dropout
- GlobalAveragePooling + Dense layers
- Final layer: Softmax (7 outputs)

### ⚙️ Training Summary

| Parameter   | Value           |
|-------------|------------------|
| Optimizer   | Adam             |
| Loss        | Sparse Categorical Crossentropy |
| Epochs      | ~30 (adjustable) |
| Accuracy    | ~72% (Train), ~63% (Test) |

---

## 📷 Real-Time Emotion Detection

The backend uses `OpenCV` to capture webcam frames, and:
- Preprocesses each frame
- Runs it through the model
- Sends annotated frames with emotion labels back to the frontend

---

## 📦 Tech Stack

| Layer     | Tools Used                           |
|-----------|--------------------------------------|
| Frontend  | React, Axios, HTML/CSS               |
| Backend   | Flask, OpenCV, TensorFlow/Keras      |
| ML Model  | CNN trained on FER-2013 dataset      |
| Others    | CORS, Git, GitHub                    |

---





## 🧑‍💻 Author

- GitHub: [Gokuzz](https://github.com/Gokuzz)
- Project: [Emotion Detection](https://github.com/Gokuzz/emotion_detection)