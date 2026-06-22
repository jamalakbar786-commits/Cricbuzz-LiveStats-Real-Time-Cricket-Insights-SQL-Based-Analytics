import requests

RAPID_API_KEY = "4b403bbba0msh284e1d055ba3e99p196e25jsnad6940874afd"

HEADERS = {
    "x-rapidapi-key": RAPID_API_KEY,
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

def get_live_matches():

    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()

def get_recent_matches():

    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()

def get_upcoming_matches():

    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()

def get_player_batting(player_id):

    url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{player_id}/batting"

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()


def get_player_bowling(player_id):

    url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{player_id}/bowling"

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()

def search_player(player_name):

    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"

    querystring = {
        "plrN": player_name
    }

    response = requests.get(
        url,
        headers=HEADERS,
        params=querystring
    )

    return response.json()

def get_player_profile(player_id):

    url = (
        f"https://cricbuzz-cricket.p.rapidapi.com/"
        f"stats/v1/player/{player_id}"
    )

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()

def get_team_players(team_id):

    url = (
        f"https://cricbuzz-cricket.p.rapidapi.com/"
        f"teams/v1/{team_id}/players"
    )

    response = requests.get(
        url,
        headers=HEADERS
    )

    return response.json()