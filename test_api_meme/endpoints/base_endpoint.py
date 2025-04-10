import requests

class BaseEndpoint:
    BASE_URL = "http://167.172.172.115:52355"

    def __init__(self, token):
        self.headers = {"Authorization": token}

