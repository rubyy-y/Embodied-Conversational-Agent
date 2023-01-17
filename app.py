from flask import Flask, render_template, request, jsonify
from chat import get_response
from api import exists, get_stats
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
    # status = {"status": existing}
    user = {"status": existing}

    # if user does exist
    if existing.startswith("viewing"):
    # get: matches, minutesPlayed, wins, winRate, kills, kd
        matches = get_stats(username, 'matches')
        minutesPlayed = get_stats(username, 'minutesPlayed')
        wins = get_stats(username, 'wins')
        winRate = get_stats(username, 'winRate')
        kills = get_stats(username, 'kills')
        kd = get_stats(username, 'kd')

        user = {"status": existing,
                "matches": matches,
                "minutesPlayed": minutesPlayed,
                "wins": wins,
                "winRate": winRate,
                "kills": kills,
                "kd": kd}

    # return jsonify(status)
    # print(user)
    return jsonify(user)

if __name__ == "__main__":
    app.run()