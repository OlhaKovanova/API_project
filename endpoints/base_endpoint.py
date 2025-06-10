import requests


class BaseEndpoint:
    BASE_URL = "http://167.172.172.115:52355"

    def __init__(self, token):
        self.headers = {"Authorization": token}

    def _get(self, path):
        url = f"{self.BASE_URL}{path}"
        return requests.get(url, headers=self.headers)

    def _post(self, path, json=None):
        url = f"{self.BASE_URL}{path}"
        return requests.post(url, headers=self.headers, json=json)

    def _put(self, path, json=None):
        url = f"{self.BASE_URL}{path}"
        return requests.put(url, headers=self.headers, json=json)

    def _delete(self, path):
        url = f"{self.BASE_URL}{path}"
        return requests.delete(url, headers=self.headers)
