from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)
app.debug = True

@app.get("/")
def index():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json(force=True).get("message")
    response = get_response(text)
    message = {"answer": response[0]}
    return jsonify(message)

if __name__ == "__main__":
    app.run()