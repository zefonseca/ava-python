# ava-python : A Python implementation of the AVA API
# Author: https://github.com/zefonseca/
# License MIT


import avaconfig
import requests
import json
import random


def ava_call(url, method, params=None):

    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 1
    }

    response = requests.post(url, json=payload).json()

    if "error" in response:
        print(response["error"]["message"])
        return

    return response["result"]


def ava_post(url, params=None):
    return requests.post(url, params)