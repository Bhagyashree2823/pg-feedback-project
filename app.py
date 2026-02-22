from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)