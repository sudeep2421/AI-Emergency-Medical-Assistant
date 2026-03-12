from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Create Flask App
app = Flask(__name__)
CORS(app)

# Load ML Model
model = pickle.load(open("model.pkl","rb"))

# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    fever = data["fever"]
    cough = data["cough"]
    headache = data["headache"]
    fatigue = data["fatigue"]
    vomiting = data["vomiting"]

    features = np.array([[fever,cough,headache,fatigue,vomiting]])

    prediction = model.predict(features)[0]

    # First Aid Suggestions
    first_aid = {
        "Flu": "Drink warm fluids, rest, and take paracetamol.",
        "Cold": "Stay hydrated, inhale steam, and rest.",
        "Dengue": "Drink plenty of fluids and consult doctor immediately.",
        "Malaria": "Seek medical attention quickly.",
        "Migraine": "Rest in a quiet dark room and drink water."
    }

    advice = first_aid.get(prediction, "Consult a doctor for proper diagnosis.")

    return jsonify({
        "disease": prediction,
        "first_aid": advice
    })

# Run Server
if __name__ == "__main__":
    app.run(debug=True)