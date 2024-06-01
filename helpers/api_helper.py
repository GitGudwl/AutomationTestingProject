import requests

class ApiHelper:
    BASE_URL = "https://dummyapi.io/data/v1"
    APP_ID = "6636324525a5b823ed8a1d31"  # Replace with your DummyAPI.io App-ID

    @staticmethod
    def get_headers():
        return {
            "app-id": ApiHelper.APP_ID,
            "Content-Type": "application/json"
        }

    @staticmethod
    def get(endpoint):
        url = f"{ApiHelper.BASE_URL}{endpoint}"
        response = requests.get(url, headers=ApiHelper.get_headers())
        return response

    @staticmethod
    def post(endpoint, data):
        url = f"{ApiHelper.BASE_URL}{endpoint}"
        response = requests.post(url, json=data, headers=ApiHelper.get_headers())
        return response

    @staticmethod
    def put(endpoint, data):
        url = f"{ApiHelper.BASE_URL}{endpoint}"
        response = requests.put(url, json=data, headers=ApiHelper.get_headers())
        return response

    @staticmethod
    def delete(endpoint):
        url = f"{ApiHelper.BASE_URL}{endpoint}"
        response = requests.delete(url, headers=ApiHelper.get_headers())
        return response
