function startListening() {
  const status = document.getElementById("status");
  const result = document.getElementById("result");

  if (!('webkitSpeechRecognition' in window)) {
    alert("Your browser doesn't support speech recognition.");
    return;
  }

  const recognition = new webkitSpeechRecognition();
  recognition.lang = "en-US";
  recognition.start();

  status.textContent = "Listening...";

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    status.textContent = "You said: " + transcript;

    fetch("/diagnose", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: transcript })
    })
    .then(res => res.json())
    .then(data => {
      result.textContent = data.result;
    });
  };

  recognition.onerror = function(err) {
    console.log(err);
    
    status.textContent = "Error recognizing speech.";
  };
}
