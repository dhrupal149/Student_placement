import streamlit as st
import requests

st.title("Placement Prediction")

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
aptitude = st.slider("Aptitude Score", 0, 100, 70)
communication = st.slider("Communication Score", 1, 10, 5)
projects = st.slider("Number of Projects", 0, 5, 2)

if st.button("Predict"):
    url = "http://localhost:3000/predict"
    data = {
        "cgpa": cgpa,
        "aptitude": aptitude,
        "communication": communication,
        "projects": projects
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        if prediction == 1:
            st.success("The student is likely to be placed.")
        else:
            st.error("The student is unlikely to be placed.")
    else:
        st.error("Error in prediction. Please try again.")