import json
import requests

key = 'e3b9db5e-0368-41a1-966f-5bee6a63ec84'

def exists(username):
    url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}"
    quest = json.loads(requests.get(url, headers={'Authorization': key}).content)
    if quest['status'] == 200:
        return f"viewing profile of {username}"
    else:
        return "This user does not exist."

def user_stats(username):
    url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}"
    quest = json.loads(requests.get(url, headers={'Authorization': key}).content)
    return quest


#### DATA EXPLORATION ####

# Structure of aquired dict object:
# user (dict): ['status', 'data']
    # status (int): connection status
    # data (dict): ['account', 'battlePass', 'image', 'stats']
        # account (dict): ['id', 'name']
            # id (str): userid
            # name (str): username
        # battlePass (dict): ['level', 'progress']
            # level (int): current level
            # progress (int): current progress
        # image (NoneType)
        # stats (dict): ['all', 'keyboardMouse', 'gamepad', 'touch']
            # all (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
            # keyboardMouse (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
            # gamepad (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
            # touch (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
                # >>> overall (dict): ['score', 'scorePerMin', 'scorePerMatch', 'wins', 'top3', 'top5', 'top6', 'top10', 'top12', 'top25', 'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 'kd', 'matches', 'winRate', 'minutesPlayed', 'playersOutlived', 'lastModified']
                # >>> solo (dict):    ['score', 'scorePerMin', 'scorePerMatch', 'wins', 'top10', 'top25', 'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 'kd', 'matches', 'winRate', 'minutesPlayed', 'playersOutlived', 'lastModified']
                # >>> duo (dict):     ['score', 'scorePerMin', 'scorePerMatch', 'wins', 'top5', 'top12', 'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 'kd', 'matches', 'winRate', 'minutesPlayed', 'playersOutlived', 'lastModified']
                # >>> trio (NoneType)
                # >>> squad (dict):   ['score', 'scorePerMin', 'scorePerMatch', 'wins', 'top3', 'top6', 'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 'kd', 'matches', 'winRate', 'minutesPlayed', 'playersOutlived', 'lastModified']
                # >>> ltm (dict):     ['score', 'scorePerMin', 'scorePerMatch', 'wins', 'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 'kd', 'matches', 'winRate', 'minutesPlayed', 'playersOutlived', 'lastModified']

# status = us['status']
# data = us['data']

# account = data['account']
# battlePass = data['battlePass']
# image = data['image']
# stats = data['stats']

# id = account['id']
# name = account['name']
# level = battlePass['level']
# progress = battlePass['progress']
# all = stats['all']
# keyboardMouse = stats['keyboardMouse']
# gamepad = stats['gamepad']
# touch = stats['touch']

# input = input('Input user name: ')
input = 'p-six'

if not exists(input):
    raise KeyError('User does not Exist!')
else:
    us = user_stats(username=input)


def get_data(key):
    data = us['data']
    account = data['account']
    battlePass = data['battlePass']

    id = account['id']
    name = account['name']
    level = battlePass['level']
    progress = battlePass['progress']

    if key == 'id':
        return id
    elif key == 'name':
        return name
    elif key == 'level':
        return level
    elif key == 'progress':
        return progress
    else:
        return "enter valid key: 'id', 'name', 'level', 'progress'"

def get_stats(method, mode):
    data = us['data']
    stats = data['stats']

    if method == 'all':
        key = stats['all']
    elif method == 'keyboardMouse':
        key = stats['keyboardMouse']
    elif method == 'gamepad':
        key = stats['gamepad']
    elif method == 'touch':
        key = stats['touch']
    else:
        return "enter valid method: 'all', 'keyboardMouse', 'gamepad', 'touch'"

    if mode == 'overall':
        return key['overall']
    elif mode == 'solo':
        return key['solo']
    elif mode == 'duo':
        return key['duo']
    elif mode == 'squad':
        return key['squad']
    elif mode == 'ltm':
        return key['ltm']
    else:
        return "enter valid mode: 'overall', 'solo', 'duo', 'squad', 'ltm'"

