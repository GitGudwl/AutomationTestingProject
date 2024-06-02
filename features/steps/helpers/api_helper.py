import requests

class ApiHelper:
    BASE_URL = "https://dummyapi.io/data/v1"
    ENDPOINT = ""
    APP_ID = ""

    @classmethod
    def set_endpoint(cls,user_id="",type = 0):
        if user_id == "" and type ==0:
            cls.ENDPOINT = "/user/create"
        elif user_id == "" and type ==1:
            cls.ENDPOINT = "/user"
        else:
            cls.ENDPOINT = f"/user/{user_id}"
        

    @classmethod
    def set_app_id(cls, app_id):
        cls.APP_ID = app_id  

    @staticmethod
    def get_headers():
        return {
            "app-id": ApiHelper.APP_ID,
            "Content-Type": "application/json"
        }

    @staticmethod
    def get():
        url = f"{ApiHelper.BASE_URL}{ApiHelper.ENDPOINT}"
        response = requests.get(url, headers=ApiHelper.get_headers())
        return response

    @staticmethod
    def post(data):
        url = f"{ApiHelper.BASE_URL}{ApiHelper.ENDPOINT}"
        response = requests.post(url, json=data, headers=ApiHelper.get_headers())
        return response

    @staticmethod
    def put(data):
        url = f"{ApiHelper.BASE_URL}{ApiHelper.ENDPOINT}"
        response = requests.put(url, json=data, headers=ApiHelper.get_headers())
        return response

    @staticmethod
    def delete():
        url = f"{ApiHelper.BASE_URL}{ApiHelper.ENDPOINT}"
        response = requests.delete(url, headers=ApiHelper.get_headers())
        return response
