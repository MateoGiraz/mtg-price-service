from fastapi import FastAPI
from service.price_service import get_prices
from repository.connection import connect

app = FastAPI()

@app.get("/price")
async def get_card(name: str = "", edition: str = ""):
    session = connect("postgresql://postgres:secret@localhost:5432/prices")
    prices = get_prices(name, edition, session)
    return list(map(lambda price: price.to_dict(), prices))