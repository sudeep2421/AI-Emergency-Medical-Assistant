import streamlit as st
import pickle
import numpy as np

# Page settings
st.set_page_config(page_title="AI Medical Assistant", layout="wide")

# Custom CSS
st.markdown("""
<style>

body {
background: linear-gradient(135deg,#1e3c72,#2a5298);
}

h1 {
text-align:center;
color:white;
}

.card {
background:white;
padding:20px;
border-radius:10px;
box-shadow:0 6px 15px rgba(0,0,0,0.2);
margin-bottom:20px;
}

div.stButton > button {
background:#ff4b2b;
color:white;
border-radius:8px;
height:40px;
width:200px;
font-size:16px;
}

div.stButton > button:hover {
background:#ff2e00;
}

.chatbox {
background:white;
padding:15px;
border-radius:10px;
box-shadow:0 6px 15px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🚑 AI Emergency Medical Assistant")

# Load model
model = pickle.load(open("model.pkl","rb"))

# Layout columns
col1, col2 = st.columns([2,1])

# ---------------------------
# LEFT SIDE (Prediction)
# ---------------------------
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("🧑 Symptoms")

    fever = st.checkbox("Fever")
    cough = st.checkbox("Cough")
    headache = st.checkbox("Headache")
    fatigue = st.checkbox("Fatigue")
    vomiting = st.checkbox("Vomiting")

    if st.button("Predict Disease"):

        features = np.array([[int(fever), int(cough), int(headache), int(fatigue), int(vomiting)]])
        prediction = model.predict(features)[0]

        first_aid = {
            "Flu": "Drink warm fluids and rest.",
            "Cold": "Stay hydrated and inhale steam.",
            "Dengue": "Drink plenty of fluids and consult doctor immediately.",
            "Malaria": "Seek medical attention quickly.",
            "Migraine": "Rest in a quiet dark room."
        }

        st.success("Possible Disease: " + prediction)
        st.info("First Aid Advice: " + first_aid.get(prediction,"Consult a doctor"))

    st.markdown('</div>', unsafe_allow_html=True)

    # Emergency card
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🚑 Emergency Help")

    st.markdown("[🏥 Find Nearby Hospital](https://www.google.com/maps/search/hospital/)")

    st.markdown("📞 **Call Ambulance: 108**")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# RIGHT SIDE (Chatbot)
# ---------------------------
with col2:

    st.markdown('<div class="chatbox">', unsafe_allow_html=True)

    st.header("🤖 Medical Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Ask a health question")

    if st.button("Send"):

        text = user_input.lower()

        if "fever" in text:
            response = "Drink fluids, rest, and monitor temperature."

        elif "burn" in text:
            response = "Cool the burn with running water for 10 minutes."

        elif "cut" in text:
            response = "Clean the wound and apply antiseptic."

        elif "headache" in text:
            response = "Rest in a quiet place and drink water."

        else:
            response = "Please consult a doctor for accurate medical advice."

        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Doctor AI", response))

    for sender, msg in st.session_state.messages:
        st.write(f"**{sender}:** {msg}")

    st.markdown('</div>', unsafe_allow_html=True)
