from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Home page (feedback form)
@app.route("/")
def home():
    return render_template("index.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    stay = request.form["stay"]
    rating = request.form["rating"]
    cleanliness = request.form["cleanliness"]
    food = request.form["food"]
    suggestions = request.form["suggestions"]

    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Stay: {stay}\n")
        f.write(f"Rating: {rating}\n")
        f.write(f"Cleanliness: {cleanliness}\n")
        f.write(f"Food: {food}\n")
        f.write(f"Suggestions: {suggestions}\n")
        f.write("-" * 30 + "\n")

    return "<h2>Thank you! Your feedback has been saved.</h2>"

# 🔐 Admin page to see all feedbacks
@app.route("/admin")
def admin():
    try:
        with open("feedback.txt", "r", encoding="utf-8") as f:
            content = f.read().replace("\n", "<br>")
    except FileNotFoundError:
        content = "No feedback yet."

    return f"""
    <h1>All Feedbacks</h1>
    <div style="font-family: monospace; white-space: pre-wrap;">
        {content}
    </div>
    """

# Render deployment (important)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)