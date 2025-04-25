from bbmirror_client import bdp

data = {
    "tickers": ["AAPL US EQUITY"],
    "fields": ["PX_LAST"],
    "options": {},
    "overrides": []
}

response = bdp(data)

if response.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)
