from flask import Flask, render_template, request, jsonify
from utils import get_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "")

    answer, model = get_answer(query)

    return jsonify({
        "answer": answer,
        "model": model
    })

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=7860)