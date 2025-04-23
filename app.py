import streamlit as st
import numpy as np
import joblib
from utils import get_input_array

# Load the trained model
model = joblib.load("aqi_model.pkl")

st.title("Air Quality Index (AQI) Prediction App 🌍")

# Input fields
co = st.number_input("CO (mg/m³)", min_value=0.0)
no2 = st.number_input("NO2 (µg/m³)", min_value=0.0)
o3 = st.number_input("O3 (µg/m³)", min_value=0.0)
t = st.number_input("Temperature (°C)", min_value=-50.0)
rh = st.number_input("Relative Humidity (%)", min_value=0.0)
ah = st.number_input("Absolute Humidity", min_value=0.0)

if st.button("Predict AQI"):
    features = get_input_array(co, no2, o3, t, rh, ah)
    prediction = model.predict(features)
    st.success(f"Predicted AQI Value: {prediction[0]:.2f}")
