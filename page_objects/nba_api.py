import requests
import json


class NBAApi:
    """
    Abstracts the NBA API
    """

    def __init__(self):
        """
        Initializes with the nba api, and the path to the 2019-2020 all star
        roster api endpoint
        """
        self.uri = "http://data.nba.net/"
        self.all_star_path = "10s/prod/v1/allstar/2019/AS_roster.json"
        self.data = {}

    def call_all_stars(self):
        """
        Using requests, makes call to nba api to the all star roster path
        """
        req = requests.get(self.uri + self.all_star_path)

        # Check if api call was successful
        if not req.ok:
            print("api call failed")
            return False
        # If api call succeeded, make self.data the parsed json response
        else:
            self.data = req.json()

    def return_all_star_names(self):
        """
        Parses the json response from all stars api and returns a list of the
        first and last names.
        """
        stars = []
        if len(self.data) == 0:
            print("No data found")
        else:
            stars_array = self.data['sportsContent']['roster'][
                0]['players']['1610616834']
            for star in stars_array:
                name = f"{star['firstName']} {star['lastName']}"
                stars.append(name)
        return stars

