import json
import requests

key = 'e3b9db5e-0368-41a1-966f-5bee6a63ec84'

def exists(username):
    url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}"
    quest = json.loads(requests.get(url, headers={'Authorization': key}).content)
    if quest['status'] == 200:
        return f"viewing profile of {username}."
    if quest['status'] == 400:
        return "Invalid or missing parameter(s)."
    if quest['status'] == 403:
        return "Account stats are private."
    if quest['status'] == 404:
        return "This user does not exist or has no stats."


def user_stats(username):
    url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}"
    quest = json.loads(requests.get(url, headers={'Authorization': key}).content)
    return quest


def get_user_data(username, info):
    """
    returns playerspecific information
    username: name of user
    info: desired information
    """

    # check if user exists
    if exists(username) == "This user does not exist.":
        raise KeyError("This user does not exist.")
    
    # if it does, check if info key available
    else:
        data = user_stats(username)['data']
        if info not in ['id', 'name', 'level', 'progress']:
            raise KeyError("Enter valid info key: ['id', 'name', 'level', 'progress']")

        elif info == 'id':
            return data['account']['id']
        elif info == 'name':
            return data['account']['name']
        elif info == 'level':
            return data['battlePass']['level']
        elif info == 'progress':
            return data['battlePass']['progress']


def get_stats(username, data, stats_key='all', type='overall'):
    """
    method returns given statistic for username
    username: name of user
    stats_key: ['all', 'keyboardMouse', 'gamepad', 'touch'] // def. 'all'
    type: ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm'] // def. 'overall'
    data: type of statistic

    """
    # check if user exists
    if exists(username) == "This user does not exist.":
        raise KeyError("This user does not exist.")
    
    # if it does, check if stats_key available
    else:
        stats = user_stats(username)['data']['stats']
        if not stats_key in list(stats):
            raise KeyError("Enter valid stats_key: ['all', 'keyboardMouse', 'gamepad', 'touch']")
        
        # if it is, check if type of data is available
        else:
            if not type in list(stats[stats_key]):
                raise KeyError("Enter valid type: ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']")
            
            # if it is, check if data available
            if not data in list(stats[stats_key][type]):
                raise KeyError("Enter valid type of data.")
            
            # TODO - if data is minutesPlayed, we want full time
            if data == "minutesPlayed":
                time = stats[stats_key][type]['minutesPlayed']
                days = time//1440
                time -= days*1440
                hours = time//60
                time -= hours*60
                minutes = time

                return f"{days}D {hours}H {minutes}M"

            # if it is available, return data
            else:
                # print(stats[stats_key][type][data])
                return stats[stats_key][type][data]

# __________________________________________________________________________________________
#### DATA STRUCTURE ####

# Structure of aquired dict object:
# user (dict): ['status', 'data']
    # // status (int): connection status
    # data (dict): ['account', 'battlePass', 'image', 'stats']
        # account (dict): ['id', 'name']
            # // id (str): userid
            # // name (str): username
        # battlePass (dict): ['level', 'progress']
            # // level (int): current level
            # // progress (int): current progress
        # image (NoneType)
        # stats (dict): ['all', 'keyboardMouse', 'gamepad', 'touch']
            # all (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
            # keyboardMouse (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
            # gamepad (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
            # touch (dict): ['overall', 'solo', 'duo', 'trio', 'squad', 'ltm']
                # >>> overall (dict): ['score', 'scorePerMin', 'scorePerMatch', 'wins', 
                #                      'top3', 'top5', 'top6', 'top10', 'top12', 'top25', 
                #                      'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 
                #                      'kd', 'matches', 'winRate', 'minutesPlayed', 
                #                      'playersOutlived', 'lastModified']
                # >>> solo (dict): ['score', 'scorePerMin', 'scorePerMatch', 'wins', 
                #                   'top10', 'top25', 
                #                   'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 
                #                   'kd', 'matches', 'winRate', 'minutesPlayed', 
                #                   'playersOutlived', 'lastModified']
                # >>> duo (dict): ['score', 'scorePerMin', 'scorePerMatch', 'wins', 
                #                  'top5', 'top12', 
                #                  'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 
                #                  'kd', 'matches', 'winRate', 'minutesPlayed', 
                #                  'playersOutlived', 'lastModified']
                # >>> trio (NoneType) ... explanation on api website
                # >>> squad (dict): ['score', 'scorePerMin', 'scorePerMatch', 'wins', 
                #                    'top3', 'top6',
                #                    'kills', 'killsPerMin', 'killsPerMatch', 'deaths', 
                #                    'kd', 'matches', 'winRate', 'minutesPlayed', 
                #                    'playersOutlived', 'lastModified']
                # >>> ltm (dict):     ['score', 'scorePerMin', 'scorePerMatch', 'wins', 
                #                      'kills', 'killsPerMin', 'killsPerMatch', 'deaths',
                #                      'kd', 'matches', 'winRate', 'minutesPlayed', 
                #                      'playersOutlived', 'lastModified']
# __________________________________________________________________________________________

# def news():
#     news_url = "https://fortnite-api.com/v2/news"
#     news = json.loads(requests.get(news_url, headers={'Authorization': key}).content)
#     br = news['data']['br']
#     stw = news['data']['stw']
#     creative = news['data']['creative']

#     print(list(br))
#     return list(br)

# news()


# ___________________
# ___example usage___

# username = 'p-six'
# matches = get_stats(username, 'matches')
# minutesPlayed = get_stats(username, 'minutesPlayed')
# wins = get_stats(username, 'wins')
# winRate = get_stats(username, 'winRate')
# kills = get_stats(username, 'kills')
# kd = get_stats(username, 'kd')

# print(username, matches, minutesPlayed, wins, winRate, kills, kd)