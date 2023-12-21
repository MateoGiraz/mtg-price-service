from fastapi import FastAPI
from price_service import get_prices

app = FastAPI()

@app.get("/")
async def get_card(name: str = ""):
    prices = get_prices(name)
    return prices