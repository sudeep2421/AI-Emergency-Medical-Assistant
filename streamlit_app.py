import streamlit as st
import requests

st.title("🚑 AI Emergency Medical Assistant")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")
vomiting = st.checkbox("Vomiting")

if st.button("Predict Disease"):

    data = {
        "fever": int(fever),
        "cough": int(cough),
        "headache": int(headache),
        "fatigue": int(fatigue),
        "vomiting": int(vomiting)
    }

    res = requests.post("http://127.0.0.1:5000/predict", json=data)
    result = res.json()

    st.success("Disease: " + result["disease"])
    st.info("First Aid: " + result["first_aid"])