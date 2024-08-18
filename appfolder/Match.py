import requests
from config import api_key

class Match:

    def __init__(self, date):
        self.base_url = "https://v3.football.api-sports.io/fixtures"
        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': api_key
        }
        self.date = date
        self.matchTime = None
        self.response = None
        self.matchState = 0
        self.firstTeam = None
        self.secondTeam = None

    def get_match_info(self):
        response = requests.get(f"{self.base_url}?date={self.date}", headers=self.headers)
        self.response = response.json()['response']

    def findSet_data(self):

        venue_names = ["Rams Park Stadyumu", "RAMS Park"]

        for response in self.response:
            if response['fixture']['venue']['name'] in venue_names:
                print("found")
                self.matchState = 1
                self.matchTime = response['fixture']['date'][11:16]
                self.firstTeam = response['teams']['home']['name']
                self.secondTeam = response['teams']['away']['name']