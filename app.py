from flask import Flask, render_template, request, jsonify
from chat import get_response
from api import exists
from widgets import widget

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

# def widgets():
#     text = request.get_json(force=True).get("message")
#     tag = get_response(text)[1]
#     div = widget(tag)
#     # div = {'header': tag, 'value': value}
#     print(tag)
#     return jsonify(div)


@app.post("/username")
def username():
    username = request.get_json(force=True).get("username")
    existing = exists(username)
    status = {"status": existing}
    # print(existing)
    return jsonify(status)

if __name__ == "__main__":
    app.run()