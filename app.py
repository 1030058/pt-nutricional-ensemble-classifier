# Streamlit Frontend (save this as app.py)
import streamlit as st
import requests

st.title('Food Classification App')

carbs = st.number_input('Carbohydrates [g]', 0.0, 100.0, 10.0)
fiber = st.number_input('Fiber [g]', 0.0, 50.0, 5.0)
sugars = st.number_input('Sugars [g]', 0.0, 100.0, 15.0)
proteins = st.number_input('Proteins [g]', 0.0, 100.0, 20.0)
fats = st.number_input('Fats [g]', 0.0, 100.0, 10.0)
energy = st.number_input('Energy [kcal]', 0.0, 1000.0, 250.0)
sodium = st.number_input('Sodium [mg]', 0.0, 5000.0, 300.0)

if st.button('Predict Food Category'):
    response = requests.post('http://127.0.0.1:8000/predict/', json={'Carbohydrates': carbs, 'Fiber': fiber, 'Sugars': sugars, 'Proteins': proteins, 'Fats': fats, 'Energy': energy, 'Sodium': sodium})
    response_data = response.json()  # Get response JSON
st.write("API Response:", response_data)  # Print response for debugging

if 'Predicted Category' in response_data:
    st.write('Predicted Category:', response_data['Predicted Category'])
else:
    st.write("Error: No 'Predicted Category' key in response. Check FastAPI output.")
