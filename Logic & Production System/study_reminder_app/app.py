from flask import Flask, render_template, request

app = Flask(__name__)

def should_remind_to_study(day, hour, is_playing_games):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return day in weekdays and hour >= 16 and not is_playing_games

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        day = request.form["day"]
        hour = int(request.form["hour"])
        is_playing = request.form.get("is_playing") == "on"
        
        if should_remind_to_study(day, hour, not is_playing):
            result = "✅ Hey Yasir! It's time to study 📚"
        else:
            result = "❌ No reminder needed right now."

    return render_template("index.html", result=result)
    
if __name__ == "__main__":
    app.run(debug=True)
