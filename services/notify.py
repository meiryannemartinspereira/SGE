import requests

class NotifyService:
    def __init__(self):
        self.__base_url = "https://api.notify.com/v1/"

    def send_notification(self, data):
        requests.post(
            url=f"{self.__base_url}send",
            json=data
        )