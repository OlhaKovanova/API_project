import requests

from test_api_meme.endpoints.base_endpoint import BaseEndpoint


class MemeAPI(BaseEndpoint):
    def get_all(self):
        return requests.get(f"{self.BASE_URL}/meme", headers=self.headers)

    def get_by_id(self, meme_id):
        return requests.get(f"{self.BASE_URL}/meme/{meme_id}", headers=self.headers)

    def create(self, text, url, tags, info):
        payload = {
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
        return requests.post(f"{self.BASE_URL}/meme", headers=self.headers, json=payload)

    def update(self, meme_id, text, url, tags, info):
        payload = {
            "id": meme_id,
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
        return requests.put(f"{self.BASE_URL}/meme/{meme_id}", headers=self.headers, json=payload)

    def delete(self, meme_id):
        return requests.delete(f"{self.BASE_URL}/meme/{meme_id}", headers=self.headers)