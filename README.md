# bbmirror-client

## Overview
A lightweight Python client for interacting with `bbmirror`. This client provides request helpers for the main endpoints: `bdp`, `bdh`, and `bds`. It is designed to be used from notebooks, internal scripts, or other applications without requiring the full FastAPI server.

## ⚠️ Disclaimer 
This project is intended for educational purposes only. It is designed to run locally on a machine with a valid Bloomberg Terminal installation. This tool does not redistribute any Bloomberg data and does not bypass any licensing restrictions. Use of this software is still subject to Bloomberg’s licensing terms. The author assumes no responsibility for misuse.

## Installation
Set the API base URL by creating a .env file in your project:
API_BASE_URL=http://your-fastapi-host:8000

## Usage Example

```python
from bbmirror_client import bdp

payload = {
    "tickers": ["AAPL US EQUITY"],
    "fields": ["PX_LAST"],
    "options": {},
    "overrides": []
}

response = bdp(payload)

if response.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)
```

