import requests
import json
from .config import BASE_API_URL

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

def bdp(data):
    response = requests.post(f"{BASE_API_URL}/bdp/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

def bdh(data):
    response = requests.post(f"{BASE_API_URL}/bdh/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

def bds(data):
    response = requests.post(f"{BASE_API_URL}/bds/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))


