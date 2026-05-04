function addMessage(text, type) {
    let div = document.createElement("div");
    div.className = type;
    div.innerHTML = text;

    let chat = document.getElementById("chat");
    chat.appendChild(div);

    chat.scrollTop = chat.scrollHeight;
}

async function send() {
    let input = document.getElementById("msg");
    let msg = input.value.trim();

    if (msg === "") return;

    addMessage(msg, "user");
    input.value = "";

    try {
        let response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: msg })
        });

        let data = await response.json();

        addMessage("<b>" + data.mode + "</b><br><br>" + data.answer, "ai");

        speak(data.answer);

    } catch (error) {
        addMessage("Error: " + error.message, "ai");
    }
}

/* VOICE INPUT */
function voice() {
    let SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Voice not supported");
        return;
    }

    let recognition = new SpeechRecognition();
    recognition.lang = "en-US";

    recognition.onresult = function (event) {
        let text = event.results[0][0].transcript;
        document.getElementById("msg").value = text;
        send();
    };

    recognition.start();
}

/* TEXT TO SPEECH */
function speak(text) {
    let speech = new SpeechSynthesisUtterance(text);
    speech.rate = 1;
    speech.pitch = 1;
    window.speechSynthesis.speak(speech);
}