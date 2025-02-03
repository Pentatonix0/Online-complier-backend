from flask import jsonify
from time import sleep
import requests


class Judge0API:

    # url = "https://judge0-ce.p.rapidapi.com"

    # @classmethod
    # def createSubmission(cls, body):
    #     headers = {'Content-Type': 'application/json',
    #                "x-rapidapi-host": "judge0-ce.p.rapidapi.com",
    #                "x-rapidapi-key": "ebeb36eac7msh97c8cdc4a93ec05p173108jsncb232ec76b9a"}

    #     response = requests.post(
    #         f"{cls.url}/submissions/?base64_encoded=false&wait=false&fields=*", json=body, headers=headers)
    #     print(response.status_code, response.text)
    #     print(response.json())
    #     return response.json()
    
    url = "http://92.51.45.95:2358"

    @classmethod
    def createSubmission(cls, body):
        headers = {'Content-Type': 'application/json'}

        response = requests.post(
            f"{cls.url}/submissions/?base64_encoded=true&wait=false&fields=*", json=body, headers=headers)
        print(response.status_code)
        print(response.json())
        return response.json()

    @classmethod
    def getSubmission(cls, token):
        headers = {}
        response = requests.get(
            f"{cls.url}/submissions/{token}?base64_encoded=true&wait=false&fields=*", headers=headers)
        print(response.status_code)
        print(response.text)

        return response.json()
