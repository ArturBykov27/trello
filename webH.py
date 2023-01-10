import requests
from authorization import Authorization


class Webhook:
   def __init__(self):
      self.url = "https://api.trello.com/1/webhooks/"
      self.headers = {"Accept": "application/json"}
      self.athorization = Authorization()
      self.query = {
         'callbackURL': "https://webhook.site/a1d9a6da-1885-4a7c-9ff0-6f111b96c2af",
         'idModel': self.athorization.id_model,
         'key': self.athorization.key,
         'token': self.athorization.token
          }
      self.create_webhook = requests.post(self.url, self.headers, self.query)
      self.create_webhook.raise_for_status()
      self.webhook_info = self.create_webhook.json()


