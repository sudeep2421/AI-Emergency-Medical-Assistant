import streamlit as st
import pickle
import numpy as np

st.set_page_config(layout="wide")

st.title("🚑 AI Emergency Medical Assistant")

# Load ML model
model = pickle.load(open("model.pkl","rb"))

col1, col2 = st.columns([2,1])

# LEFT PANEL
with col1:

    st.header("🧑 Symptoms")

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

# RIGHT PANEL CHATBOT
with col2:

    st.header("🤖 Medical Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Ask a medical question")

    if st.button("Send"):

        response = ""

        text = user_input.lower()

        if "fever" in text:
            response = "Drink fluids and rest."

        elif "burn" in text:
            response = "Cool the burn under running water."

        elif "cut" in text:
            response = "Clean the wound and apply antiseptic."

        elif "headache" in text:
            response = "Rest in a quiet place and drink water."

        else:
            response = "Please consult a doctor for accurate advice."

        st.session_state.messages.append(("You",user_input))
        st.session_state.messages.append(("Bot",response))

    for sender,msg in st.session_state.messages:
        st.write(f"**{sender}:** {msg}")
