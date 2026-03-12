import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="AI Emergency Medical Assistant", layout="wide")

# ----------------------------
# COLORFUL CSS DESIGN
# ----------------------------
st.markdown("""
<style>

/* Animated gradient background */
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb,#a6c1ee);
background-size:400% 400%;
animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Title */
h1{
text-align:center;
color:white;
font-weight:bold;
text-shadow:2px 2px 8px rgba(0,0,0,0.3);
}

/* Cards */
.card{
background:rgba(255,255,255,0.9);
padding:20px;
border-radius:12px;
box-shadow:0 8px 20px rgba(0,0,0,0.25);
margin-bottom:20px;
}

/* Buttons */
div.stButton > button{
background: linear-gradient(90deg,#ff512f,#dd2476);
color:white;
border:none;
border-radius:10px;
padding:10px 20px;
font-size:16px;
box-shadow:0 5px 10px rgba(0,0,0,0.3);
transition:0.3s;
}

div.stButton > button:hover{
transform:scale(1.05);
background: linear-gradient(90deg,#36d1dc,#5b86e5);
}

/* Chatbot card */
.chatbox{
background:rgba(255,255,255,0.9);
padding:15px;
border-radius:12px;
box-shadow:0 6px 18px rgba(0,0,0,0.3);
}

/* Input styling */
.stTextInput input{
border-radius:8px;
padding:10px;
border:2px solid #5b86e5;
}

/* Success message */
[data-testid="stAlert-success"]{
background:#c8f7c5;
}

/* Info message */
[data-testid="stAlert-info"]{
background:#d1ecff;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------
st.title("🚑 AI Emergency Medical Assistant")

# ----------------------------
# LOAD MODEL
# ----------------------------
model = pickle.load(open("model.pkl","rb"))

# Layout columns
col1, col2 = st.columns([2,1])

# ----------------------------
# LEFT PANEL
# ----------------------------
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

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
        "Flu":"Drink warm fluids and rest.",
        "Cold":"Stay hydrated and inhale steam.",
        "Dengue":"Drink plenty of fluids and consult doctor immediately.",
        "Malaria":"Seek medical attention quickly.",
        "Migraine":"Rest in a quiet dark room."
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

# ----------------------------
# RIGHT PANEL CHATBOT
# ----------------------------
with col2:

    st.markdown('<div class="chatbox">', unsafe_allow_html=True)

    st.header("🤖 Medical Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Ask a health question")

    if st.button("Send"):

        text = user_input.lower()

        if "fever" in text:
            response = "Drink fluids and rest."

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

    for sender,msg in st.session_state.messages:
        st.write(f"**{sender}:** {msg}")

    st.markdown('</div>', unsafe_allow_html=True)
