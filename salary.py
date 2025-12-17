import streamlit as st
import pickle
import numpy as np

# Load model and encoders
with open("salary.pkl", "rb") as f:
    model, edu_encoder, job_encoder = pickle.load(f)

st.title("💼 Salary Prediction App")
st.write("Predict Salary using Experience, Degree, and Job Title")

# Dropdown inputs
education = st.selectbox(
    "Select Education Level",
    edu_encoder.classes_
)

job = st.selectbox(
    "Select Job Title",
    job_encoder.classes_
)

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.5
)

# Encode inputs
edu_encoded = edu_encoder.transform([education])[0]
job_encoded = job_encoder.transform([job])[0]

# Predict
if st.button("Predict Salary"):
    input_data = np.array([[edu_encoded, job_encoded, experience]])
    prediction = model.predict(input_data)


    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")

