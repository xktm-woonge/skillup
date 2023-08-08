# ./model/rest_api.py

import requests

class RESTClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, method, endpoint, data=None, token=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        try:
            response = requests.request(method, url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"status": "FAIL", "message": str(e)}

    def request_verification_code(self, email):
        return self._request("POST", "register/sendEmail_api", {"email": email})

    def verify_verification_code(self, email, verification_code):
        return self._request("POST", "register/confirmCertNum_api", {"email": email, "verification_code": verification_code})

    def register_user(self, email, password, salt):
        return self._request("POST", "register/addUser_api", {"email": email, "password": password, "salt": salt})

    def login(self, email, password):
        return self._request("POST", "login_api", {"email": email, "password": password})
    
    def get_userInfo(self, email, token):
        return self._request("GET", "userInfo_api", {"email": email}, token)