# 🇵🇹 Portuguese Nutritional Ensemble Classifier

This project is a **machine learning-based food classification model** that predicts **food categories** based on their nutritional content. 
It utilizes an **ensemble approach** combining **Random Forest, Neural Network, Decision Tree, and Gradient Boosting** for improved accuracy.

## 🚀 Features

- **Automated Food Classification** using **Carbohydrates, Fiber, Sugars, Proteins, Fats, Energy, and Sodium**.
- **Ensemble Learning**: Uses multiple models for high accuracy (**95%+ accuracy**).
- **Web App**: Built with **FastAPI (backend)** and **Streamlit (frontend)**.
- **Automated Predictions**: Batch process food data from CSV files.

---

## 📦 Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Portuguese-Nutritional-Ensemble-Classifier.git
cd Portuguese-Nutritional-Ensemble-Classifier
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
- **For macOS/Linux**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
- **For Windows**:
  ```bash
  python -m venv env
  env\Scripts\activate
  ```

### 3️⃣ **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Train the Model & Save It**
```bash
python train_model.py
```
This will **train the model** and save the files:
- `food_classifier_model.pkl` (trained model)
- `scaler.pkl` (data preprocessor)
- `label_encoder.pkl` (category encoder)

### 5️⃣ **Run the Web App**
- **Start FastAPI Backend**:
  ```bash
  uvicorn api:app --reload
  ```
- **Start Streamlit Frontend**:
  ```bash
  streamlit run app.py
  ```

### 6️⃣ **Automate Batch Predictions**
```bash
python automate_predictions.py
```
This will generate **`predictions.csv`**, containing food category predictions.

---

## 📊 Example Usage

### **Using the API**

You can send a **POST request** to **FastAPI** with food nutrition details:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{
  "Carbohydrates": 25.5,
  "Fiber": 4.3,
  "Sugars": 5.1,
  "Proteins": 12.0,
  "Fats": 8.0,
  "Energy": 250,
  "Sodium": 300
}'
```
Response:
```json
{"Predicted Category": "Cereais e produtos à base de cereais"}
```

---

## 🛠 Technologies Used

- **Python** 🐍
- **Scikit-Learn** (Machine Learning)
- **FastAPI** (Backend API)
- **Streamlit** (Frontend UI)
- **Joblib** (Model Saving)
- **Pandas & NumPy** (Data Processing)
- **Imbalanced-Learn** (SMOTE for Class Balancing)

---

## 💡 Future Improvements

✅ **Deploy to Cloud** (e.g., Heroku, AWS, or Docker)  
✅ **Expand Model with More Features** (e.g., Vitamins, Minerals)  
✅ **Create a Mobile App Version**  

---

## 🤝 Contributing

1. **Fork this repository**.
2. **Create a feature branch** (`git checkout -b new-feature`).
3. **Commit your changes** (`git commit -m "Added a new feature"`).
4. **Push to GitHub** (`git push origin new-feature`).
5. **Create a Pull Request**.

---

## 🏆 Credits

Developed by **[Your Name]** 🚀  
For research and **nutritional data classification** in Portugal.  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🌎 Connect with Me

🔗 [LinkedIn](https://www.linkedin.com/in/YOUR_LINKEDIN)  
🐙 [GitHub](https://github.com/YOUR_GITHUB_USERNAME)  
✉️ Email: your_email@example.com  
