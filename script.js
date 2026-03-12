document.getElementById("symptomForm").addEventListener("submit", function (e) {

    e.preventDefault();

    const data = {

        fever: document.getElementById("fever").checked ? 1 : 0,
        cough: document.getElementById("cough").checked ? 1 : 0,
        headache: document.getElementById("headache").checked ? 1 : 0,
        fatigue: document.getElementById("fatigue").checked ? 1 : 0,
        vomiting: document.getElementById("vomiting").checked ? 1 : 0

    };

    fetch("http://127.0.0.1:5000/predict", {

        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    })

        .then(res => res.json())
        .then(result => {

            document.getElementById("result").innerHTML =

                "Possible Disease: " + result.disease +
                "<br><br>First Aid: " + result.first_aid;

        });

});


function sendMessage() {

    let input = document.getElementById("userInput").value.toLowerCase();
    let chatlogs = document.getElementById("chatlogs");

    chatlogs.innerHTML += "<p><b>You:</b> " + input + "</p>";

    let response = "";

    if (input.includes("fever"))
        response = "Drink fluids and rest.";

    else if (input.includes("burn"))
        response = "Cool the burn under running water.";

    else if (input.includes("cut"))
        response = "Clean the wound and apply antiseptic.";

    else
        response = "Consult a doctor for accurate medical advice.";

    chatlogs.innerHTML += "<p><b>Bot:</b> " + response + "</p>";

    document.getElementById("userInput").value = "";

    chatlogs.scrollTop = chatlogs.scrollHeight;

}


function findHospital() {

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(function (position) {

            let lat = position.coords.latitude;
            let lon = position.coords.longitude;

            window.open(
                "https://www.google.com/maps/search/hospital/@" + lat + "," + lon + ",15z"
            );

        });

    }

}