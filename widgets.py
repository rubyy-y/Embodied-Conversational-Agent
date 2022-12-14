# use get_response only tempotarily to mimic behaviour of function
from chat import get_response

from api import get_user_data, get_stats

# idea of this file: handle arias tags after in get_response in app.py predict()
# maybe functions could return html divisions inside base.html

# user data - name, id, level, progress

# static widgets - score, scorePerMin, scorePerMatch, wins, topk,
#                  kills, killsPerMin, killsPerMatch, deaths, kd,
#                  matches, winRate, minutesPlayed, playersOutlived // all of these are also intent tags

def widget(tag): # response[1]
    """
    function receives tag from intents.json
    creates corresponding division objects in html
    """
    if tag in ['joke', 'greeting', 'thanks']: # add non action tags
        pass

    else:
        username='p-six'
        data = tag
        # stats_key='all'
        # type='solo'

        div = { "header": tag, "value": get_stats(username, data) }
        return div


# print(get_stats('p-six', 'minutesPlayed'))