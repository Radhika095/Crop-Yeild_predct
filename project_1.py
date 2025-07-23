import streamlit as st
import numpy as np
import joblib

# Title
st.title("🌿 Sustainable Crop Yield Prediction Model")

# Load trained model safely
model_path = r"C:\Users\Acer\OneDrive\Desktop\python project\crop_yield_prediction_Output_Cal.pkl"
try:
    crop_yield_model = joblib.load(model_path)
except FileNotFoundError:
    st.error("⚠️ Model file not found. Please check the path.")
    st.stop()

# Collect user inputs
year = st.number_input("Enter the year:", min_value=0.0, max_value=60.0)
rainfall = st.number_input("Enter average rainfall (mm/year):", min_value=0.0, max_value=2000.0)
pesticides = st.number_input("Enter pesticides usage (tonnes):", min_value=0.0)
temperature = st.number_input("Enter average temperature (°C):", min_value=0.0, max_value=30.0)

# Button trigger for prediction
if st.button("📈 Predict Crop Yield"):
    input_data = np.array([[year, rainfall, pesticides, temperature]])
    try:
        prediction = crop_yield_model.predict(input_data)
        st.success(f"🌾 Predicted Crop Yield: {float(prediction[0]):.2f} W")
        st.write("Thank you for using the model!")
    except Exception as e:
        st.error(f"Prediction failed due to: {e}")