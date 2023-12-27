from fastapi import FastAPI
from service.price_service import get_prices
from repository.connection import connect

app = FastAPI()

@app.get("/price")
async def get_card(name: str = "", edition: str = "", foil: bool = False):
    session = connect("postgresql://postgres:secret@localhost:5432/prices")
    prices = get_prices(name, edition, foil, session)
    return list(map(lambda price: price.to_dict(), prices))