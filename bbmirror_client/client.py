import requests
import json
from .config import BASE_API_URL

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

def bdp(data):
    return requests.post(f"{BASE_API_URL}/bdp/", headers=HEADERS, data=json.dumps(data))

def bdh(data):
    return requests.post(f"{BASE_API_URL}/bdh/", headers=HEADERS, data=json.dumps(data))

def bds(data):
    return requests.post(f"{BASE_API_URL}/bds/", headers=HEADERS, data=json.dumps(data))
