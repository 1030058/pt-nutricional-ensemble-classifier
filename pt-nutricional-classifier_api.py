from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the trained ensemble model
with open("ensemble_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Convert data to DataFrame
        df = pd.DataFrame([data])
        
        # Ensure column order matches training data
        feature_columns = ["Proteínas [g]", "Hidratos de carbono [g]", "Lípidos [g]"]
        df = df[feature_columns]
        
        # Make prediction
        prediction = model.predict(df)
        predicted_category = prediction[0]
        
        return jsonify({"Predicted Category": predicted_category})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
