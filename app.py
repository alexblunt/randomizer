from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Список ответов
answers = ["Да", "Нет", "Скорее всего да", "Скорее всего нет", "Дай-ка подумать"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/randomize")
def randomize():
    return jsonify({"answer": random.choice(answers)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
