import datetime

from authorization import Authorization
import requests

ARTUR = "58b6e5d80ae235709ceefab5"
MARINA = "5c80e967c19bbc148fafa2b4"
YULIA = "5e33d4d6cbea3223847106ff"
KSENIA = "5c20beeae434c930084af5aa"
VIKA = "5ddcf34e36599986c8988839"
DIMA = "5f0c4f9757297d65c50a0cf7"


class Managers(Authorization):
    def __init__(self):
        super().__init__()
        self.full_list = (MARINA, KSENIA, VIKA, ARTUR, YULIA, DIMA)

    def update_current_list(self):
        with open("text.txt", "r") as q:
            self.current_list = [globals()[line.strip()] for line in q]

    def assign_manage(self, card_id):
        self.url = f"https://api.trello.com/1/cards/{card_id}/idMembers"
        self.query = {
        'key': self.key,
        'token': self.token,
        "value": self.current_list[0]
            }
        self.response = requests.post(self.url, params=self.query)
        self.response.raise_for_status()
        self.remove_manage()
        return self.response.json()

    def remove_manage(self):
        with open("text.txt", "r") as q:
            lines = q.readlines()
        lines.pop(0)
        with open("text.txt", "w") as q:
            q.writelines(lines)
        print("Remove", self.current_list[0])

    def restore_list(self):
        today = datetime.date.today().strftime("%d%m%Y")
        tab = requests.get(url="https://api.sheety.co/7dc395588fff5901e0d17afdfffa07a5/1CQueue/лист1")
        for name in tab.json()['лист1']:
            with open("text.txt", "a") as queue:
                queue.write(name[f"{today}"])
                queue.write("\n")

    def is_need_assign_managers(self, member_id):
        if member_id not in self.full_list:
            return True
        else:
            return False




