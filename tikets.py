import requests
from authorization import Authorization

class Tikets(Authorization):
    def __init__(self):
        super().__init__()
        self.url = "https://api.trello.com/1/lists/565432005e7e3f7ebcc4a09d/cards"
        self.query = {
        'key': self.key,
        'token': self.token
            }

    def get_tikets(self):
        self.response = requests.get(self.url, params=self.query)
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data

    def is_need_assign_label(self, label_name):
        if "1C" in label_name:
            return True
        else:
            pass



