from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = "replace-this-with-a-secret"  # replace or use env var in production

@app.route("/")
def index():
    projects = [
        {"title": "Project A", "description": "This project is a simple web scraper built with Python that automatically fetches the latest news headlines from a public website (e.g., BBC News) and saves them into a text file.", "link": "https://github.com/AnitaByteCraft/task-03-web-scraper.git"},
        {"title": "Project B", "description": "This project performs a basic data analysis of sales data using Python and Pandas.We analyzed sales trends, top products, and regional performance.", "link": "https://github.com/AnitaByteCraft/task-05-data-analysis.git"}
    ]
    return render_template("index.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        message = request.form.get("message", "")

        # Save message to CSV (simple persistent store)
        os.makedirs("data", exist_ok=True)
        with open("data/messages.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, email, message])

        flash("Thanks! Your message has been received.")
        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
