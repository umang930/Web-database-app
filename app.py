from flask import Flask, request, render_template_string
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client["student_db"]
students = db["students"]

@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as file:
        return render_template_string(file.read())

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")

    students.insert_one({
        "name": name,
        "email": email
    })

    return "Student registered successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)