from requests import get, post
import json

from requests.api import request


ENDPOINT = "http://localhost:5000"


def login(username, password):
    route = "api/login"
    query = "{}/{}".format(ENDPOINT, route)
    body = {"username": username, "password": password}
    response = post(query, json=body)

    return response.json()
