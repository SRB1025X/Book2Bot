from flask import Flask, request, render_template, jsonify
from utils.ocr import extract_text_from_file
from utils.ingestion import embed_and_store
from utils.chatbot import ask_question
from pymongo import MongoClient
import os
from config import MONGO_URI, DB_NAME

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        text = extract_text_from_file(file)
        embed_and_store(text)
        return render_template("index.html", message="File processed and stored.")
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = ask_question(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)