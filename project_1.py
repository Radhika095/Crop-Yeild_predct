import streamlit as st 
import numpy as np 
import joblib as jb 

# Title of the app
st.title("Welcome To Sustainable Crop Yield Prediction...!")

# Load the trained model
model_path = (r"C:\Users\Acer\OneDrive\Desktop\pyhton project\crop_yield_prediction_Output_Cal.pkl")
crop_yield_model = jb.load(model_path)

# User inputs
exp_1 = st.number_input("Enter the Year:")
exp_2 = st.number_input("Enter the average rainfall in mm per year:")
exp_3 = st.number_input("Enter the pesticides in tonnes:")
exp_4 = st.number_input("Enter the average temperature (°C):", min_value=0.0, max_value=25.0)

# Predict button
if st.button("Predict Crop Yield"):
    new_data = np.array([[exp_1, exp_2, exp_3, exp_4]])
    prediction = crop_yield_model.predict(new_data)
    st.success(f"🌾 The predicted sustainable crop yield is: {float(prediction[0]):.2f} INR")
    st.info("Thank you for using the app!")