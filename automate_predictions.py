import pandas as pd
import numpy as np
import joblib

# Load the trained model and preprocessors
model = joblib.load("food_classifier_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Load the CSV file containing food nutrition data
input_csv = "food_nutrition_data.csv"  # Update with actual file path
df = pd.read_csv(input_csv)

# Ensure correct column names
expected_columns = ["Carbohydrates [g]", "Fiber [g]", "Sugars [g]", "Proteins [g]", "Fats [g]", "Energy [kcal]", "Sodium [mg]"]
if not all(col in df.columns for col in expected_columns):
    raise ValueError("Input CSV must contain the correct columns: " + ", ".join(expected_columns))

# Fill missing values with median (consistent with training)
df.fillna(df.median(), inplace=True)

# Scale the features
features_scaled = scaler.transform(df[expected_columns])

# Make predictions
predictions = model.predict(features_scaled)

# Convert predictions back to category names
predicted_categories = label_encoder.inverse_transform(predictions)

# Save results to a new CSV file
df["Predicted Category"] = predicted_categories
output_csv = "predictions.csv"
df.to_csv(output_csv, index=False)

print(f"Predictions saved to {output_csv}")
