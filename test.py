from fastdata_client.clients.bloomberg import bdp
from fastdata_client.clients.gie import get_lng_lso

# data_bb = {
#     "tickers": ["AAPL US EQUITY"],
#     "fields": ["PX_LAST"],
#     "options": {},
#     "overrides": []
# }

data_gie = {
    "target": "fluxys_lng",
    "start_date": "2020-01-01",
    "end_date": "2022-07-10"
}

# response_bb = bdp(data_bb)
response_gie = get_lng_lso(data_gie)

# print(response_bb)
print(response_gie)