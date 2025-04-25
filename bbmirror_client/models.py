from pydantic import BaseModel
from typing import List, Dict, Any

class BdpRequest(BaseModel):
    tickers: List[str]
    fields: List[str]
    options: Dict[str, Any] = {}
    overrides: List[Dict[str, Any]] = []

class BdhRequest(BaseModel):
    tickers: List[str]
    fields: List[str]
    start_date: str
    end_date: str
    options: Dict[str, Any] = {}
    overrides: List[Dict[str, Any]] = []

class BdsRequest(BaseModel):
    tickers: List[str]
    field: str
    options: Dict[str, Any] = {}
    overrides: List[Dict[str, Any]] = []

class BdipRequest(BaseModel):
    ticker: str
    event_type: str = "TRADE"
    interval: int = 1
    start_datetime: str
    end_datetime: str
