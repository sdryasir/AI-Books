from datetime import datetime

# --- Knowledge Base (Facts) ---
today = datetime.now().strftime("%A")  # e.g., Monday
current_hour = datetime.now().hour     # e.g., 17 (5 PM)
is_playing_games = False               # User status

# --- Rule Engine ---
def should_remind_to_study(day, hour, gaming):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if day in weekdays and hour >= 16 and not gaming:
        return True
    return False

# --- Decision and Action ---
if should_remind_to_study(today, current_hour, is_playing_games):
    print("Hey Yasir! It's time to study 📚")
else:
    print("No reminder needed right now.")
