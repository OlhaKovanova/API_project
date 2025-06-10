from endpoints.base_endpoint import BaseEndpoint
from utils.assertions import assert_status_bad_request


class MemeAPI(BaseEndpoint):
    def get_all(self):
        return self._get("/meme")

    def get_by_id(self, meme_id):
        return self._get(f"/meme/{meme_id}")

    def create(self, text, url, tags, info):
        payload = {
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
        return self._post("/meme", json=payload)

    def update(self, meme_id, text, url, tags, info):
        payload = {
            "id": meme_id,
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
        return self._put(f"/meme/{meme_id}", json=payload)

    def delete(self, meme_id):
        return self._delete(f"/meme/{meme_id}")
