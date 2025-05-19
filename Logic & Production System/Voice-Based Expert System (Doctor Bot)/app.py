from flask import Flask, render_template, request, jsonify
import pyttsx3

app = Flask(__name__)

rules = [
    {"if": ["fever", "cough"], "then": "You may have flu. Please take rest."},
    {"if": ["sore throat"], "then": "Drink warm tea and rest your throat."},
    {"if": ["headache"], "then": "Consider hydration and light rest."},
    {"if": ["toothace"], "then": "consider taking inset."},
]

engine = pyttsx3.init()

def match_rules(symptoms):
    symptoms_set = set(symptoms)
    for rule in rules:
        if set(rule["if"]).issubset(symptoms_set):
            return rule["then"]
    return "Sorry, I couldn't understand your condition."

def speak_output(message):
    engine.say(message)
    engine.runAndWait()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.get_json()
    spoken_text = data["text"].lower()
    # Convert spoken input to symptoms list
    keywords = ["fever", "cough", "sore throat", "headache"]
    symptoms = [word for word in keywords if word in spoken_text]
    
    result = match_rules(symptoms)
    speak_output(result)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
