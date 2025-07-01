import streamlit as st
import numpy as np
import pickle
import json

# Load the trained model
model = pickle.load(open("crop_recommendation.pkl", "rb"))

# Load label mapping (target number to crop name)
with open("target_mapping.json", "r") as f:
    target_mapping = json.load(f)

# UI Title
st.markdown("<h1 style='text-align: center; color: green;'>🌱 Crop Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar Input Form
st.sidebar.markdown("### Enter the following details:")

N = st.sidebar.number_input("🧪 Nitrogen (N)", 0, 200, step=1)
P = st.sidebar.number_input("🧪 Phosphorus (P)", 0, 200, step=1)
K = st.sidebar.number_input("🧪 Potassium (K)", 0, 200, step=1)
temperature = st.sidebar.number_input("🌡️ Temperature (°C)", 0.0, 50.0, step=0.1)
humidity = st.sidebar.number_input("💧 Humidity (%)", 0.0, 100.0, step=0.1)
ph = st.sidebar.number_input("⚗️ pH Level", 0.0, 14.0, step=0.1)
rainfall = st.sidebar.number_input("🌧️ Rainfall (mm)", 0.0, 500.0, step=0.1)

# Predict Button
if st.sidebar.button("🌾 Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]  # numeric prediction

    # Convert number to crop name
    predicted_crop = target_mapping[str(prediction)]

    # Display result
    st.success(f"✅ Recommended Crop: **{predicted_crop.upper()}**")
