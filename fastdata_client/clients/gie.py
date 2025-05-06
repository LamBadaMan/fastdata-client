import requests
import json
from .config import BASE_API_URL

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

def get_gas_storage(data):
    response = requests.post(f"{BASE_API_URL}/gas_storage/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

def get_gas_company(data):
    response = requests.post(f"{BASE_API_URL}/gas_company/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

def get_gas_country(data):
    response = requests.post(f"{BASE_API_URL}/gas_country/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

def get_lng_terminal(data):
    response = requests.post(f"{BASE_API_URL}/lng_terminal/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

def get_lng_lso(data):
    response = requests.post(f"{BASE_API_URL}/lng_lso/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

def get_lng_country(data):
    response = requests.post(f"{BASE_API_URL}/lng_country/", headers=HEADERS, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))

