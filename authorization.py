import requests
import os

class Authorization:
    def __init__(self):
        self. token = os.environ["TRELLO_TOKEN"]
        self.key = os.environ['TRELLO_KEY']
        self.params = {'key': self.key, 'token': self.token}
        self.headers = {"Accept": "application/json"}
        self.authorization_response = requests.get(
            "https://api.trello.com/1/tokens/f75cc8112a3b1085b32ccccf3496b3db78385300023c5a5c4c79e88c24fcf816",
            headers=self.headers, params=self.params)
        self.authorization_response.raise_for_status()
        self.id_model = self.authorization_response.json()['permissions'][0]['idModel']
        self.auth_info = self.authorization_response.json()
