import httpx
from fastapi import HTTPException

BASE_URL = "https://api.coingecko.com/api/v3"

class CoinGeckoClient:
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=10)

    async def ping(self):
        r = await self.client.get(f"{BASE_URL}/ping")
        return r.status_code == 200

    async def list_coins(self, page: int, per_page: int):
        url = f"{BASE_URL}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "page": page,
            "per_page": per_page
        }
        r = await self.client.get(url, params=params)
        if r.status_code != 200:
            raise HTTPException(502, "Failed to fetch coins")
        return r.json()

    async def list_categories(self):
        r = await self.client.get(f"{BASE_URL}/coins/categories/list")
        if r.status_code != 200:
            raise HTTPException(502, "Failed to fetch categories")
        return r.json()

    async def coin_details(self, coin_id: str):
        r = await self.client.get(f"{BASE_URL}/coins/{coin_id}")
        if r.status_code != 200:
            raise HTTPException(404, "Coin not found")
        return r.json()

    async def markets_vs_currency(self, currency: str, page: int, per_page: int):
        url = f"{BASE_URL}/coins/markets"
        params = {
            "vs_currency": currency,
            "order": "market_cap_desc",
            "page": page,
            "per_page": per_page
        }
        r = await self.client.get(url, params=params)
        if r.status_code != 200:
            raise HTTPException(502, "Failed to fetch market data")
        return r.json()
