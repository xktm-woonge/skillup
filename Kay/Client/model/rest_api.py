# ./model/rest_api.py

import requests

class RESTClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        response = requests.request(method, url, json=data, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def request_verification_code(self, email):
        return self._request("POST", "verification_code", {"email": email})

    def verify_verification_code(self, email, verification_code):
        return self._request("POST", "verify", {"email": email, "verification_code": verification_code})

    def register_user(self, email, password, salt):
        return self._request("POST", "register", {"email": email, "password": password, "salt": salt})

    def login(self, email, password):
        return self._request("POST", "login", {"email": email, "password": password})
