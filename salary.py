import streamlit as st
import pickle
import numpy as np

# Load trained model (ONLY model)
with open("salary.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💼 Salary Prediction App")
st.write("Predict Salary based on Years of Experience")

# Optional inputs (not used for prediction)
education = st.selectbox(
    "Select Education Level",
    ["Bachelor's", "Master's", "PhD"]
)

job = st.selectbox(
    "Select Job Title",
    ["Software Engineer", "Data Analyst", "Senior Manager", "Sales Associate", "Director"]
)

# Main input used for prediction
experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.5
)

# Predict salary
if st.button("Predict Salary"):
    input_data = np.array([[experience]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")
