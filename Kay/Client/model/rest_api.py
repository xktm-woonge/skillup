# ./model/rest_api.py

import requests

class RESTClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.request(method, url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"status": "FAIL", "message": str(e)}

    def request_verification_code(self, email):
        return self._request("POST", "auth/verificationCode", {"email": email})

    def verify_verification_code(self, email, verification_code):
        return self._request("POST", "auth/verify", {"email": email, "verification_code": verification_code})

    def register_user(self, email, password, salt):
        return self._request("POST", "auth/register", {"email": email, "password": password, "salt": salt})

    def login(self, email, password):
        return self._request("POST", "auth/login", {"email": email, "password": password})