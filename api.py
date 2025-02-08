from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model & preprocessor
model = joblib.load("food_classifier_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.post("/predict/")
def predict(data: dict):
    features = np.array([[
        data["Carbohydrates"], data["Fiber"], data["Sugars"], 
        data["Proteins"], data["Fats"], data["Energy"], data["Sodium"]
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    category = label_encoder.inverse_transform(prediction)[0]

    return {"Predicted Category": category}

