from requests import get, post
import json

from requests.api import request


ENDPOINT = "http://192.168.254.114:5000"


def login(username, password):
    route = "api/login"
    query = "{}/{}".format(ENDPOINT, route)
    body = {
        "username": username,
        "password": password
    }
    response = post(query, json=body)

    return response.json()


def register(username, password, email, first_name, last_name):
    route = "api/register"
    query = "{}/{}".format(ENDPOINT, route)
    body = {
        "username": username,
        "password": password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name
    }
    response = post(query, json=body)

    return response.json()
