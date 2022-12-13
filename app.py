from flask import Flask, render_template, request, jsonify
from chat import get_response
from api import exists

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
    # print(response[0])
    return jsonify(message)

@app.post("/username")
def username():
    username = request.get_json(force=True).get("username")
    existing = exists(username)
    status = {"status": existing}
    # print(existing)
    return jsonify(status)

if __name__ == "__main__":
    app.run()