import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("aqi_model.pkl")

st.title("Air Quality Prediction App")

# Input fields for user to enter features
pm25 = st.number_input("PM2.5", min_value=0.0)
pm10 = st.number_input("PM10", min_value=0.0)
no = st.number_input("NO", min_value=0.0)
no2 = st.number_input("NO2", min_value=0.0)
nox = st.number_input("NOx", min_value=0.0)
nh3 = st.number_input("NH3", min_value=0.0)
co = st.number_input("CO", min_value=0.0)
so2 = st.number_input("SO2", min_value=0.0)
o3 = st.number_input("O3", min_value=0.0)
benzene = st.number_input("Benzene", min_value=0.0)
toluene = st.number_input("Toluene", min_value=0.0)
xylene = st.number_input("Xylene", min_value=0.0)

if st.button("Predict AQI Category"):
    # Create input array
    input_data = np.array([[pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene]])
    prediction = model.predict(input_data)

    st.success(f"Predicted AQI Category: {prediction[0]}")
