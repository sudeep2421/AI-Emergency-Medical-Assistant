import streamlit as st
import pickle
import numpy as np

st.title("🚑 AI Emergency Medical Assistant")

# load model
model = pickle.load(open("model.pkl","rb"))

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")
vomiting = st.checkbox("Vomiting")

if st.button("Predict Disease"):

    features = np.array([[int(fever),int(cough),int(headache),int(fatigue),int(vomiting)]])

    prediction = model.predict(features)[0]

    first_aid = {
        "Flu":"Drink fluids and rest.",
        "Cold":"Stay warm and hydrate.",
        "Dengue":"Drink plenty of fluids and consult doctor.",
        "Malaria":"Seek medical attention quickly.",
        "Migraine":"Rest in a quiet dark room."
    }

    st.success("Disease: " + prediction)
    st.info("First Aid: " + first_aid.get(prediction,"Consult doctor"))
