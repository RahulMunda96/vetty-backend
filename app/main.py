from fastapi import FastAPI, Depends, Query, HTTPException
from pydantic import BaseModel
from app.auth import create_access_token, fake_user_db, verify_token
from app.coingecko_client import CoinGeckoClient
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(title="Vetty Intern Crypto API", version="1.0.0")
cg = CoinGeckoClient()

class Login(BaseModel):
    username: str
    password: str



@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/version")
async def version():
    return {"version": "1.0.0"}

@app.get("/coins")
async def coins(
    page_num: int = 1,
    per_page: int = 10,
    _: str = Depends(verify_token)
):
    data = await cg.list_coins(page=page_num, per_page=per_page)
    return {"page": page_num, "per_page": per_page, "items": data}

@app.get("/categories")
async def categories(
    page_num: int = 1,
    per_page: int = 10,
    _: str = Depends(verify_token)
):
    data = await cg.list_categories()
    start = (page_num - 1) * per_page
    end = start + per_page
    return {"items": data[start:end]}

@app.get("/coins/markets")
async def coin_markets(
    vs: str = Query("inr"),
    page_num: int = 1,
    per_page: int = 10,
    _: str = Depends(verify_token)
):
    if vs not in ["inr", "cad"]:
        raise HTTPException(400, "vs must be inr or cad")

    data = await cg.markets_vs_currency(vs, page_num, per_page)
    return {"currency": vs, "page": page_num, "items": data}

@app.get("/coins/{coin_id}")
async def coin(coin_id: str, _: str = Depends(verify_token)):
    return await cg.coin_details(coin_id)
