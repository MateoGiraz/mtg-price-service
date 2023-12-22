import re
from service.scrapper import scrap
from model.card import Card

def get_prices(card_name, session):
  existing_prices = session.query(Card).filter_by(name=card_name).all()

  if existing_prices and all(data.is_fresh() for data in existing_prices):
    return existing_prices
    
  prices = scrap(card_name)
  cards = [Card(name, getDouble(price)) for name, price in prices if name == card_name]

  session.query(Card).filter_by(name=card_name).delete()

  session.add_all(cards)
  session.commit()
  
  return cards

def getDouble(price):
  numeric_string = re.sub(r'[^\d.]', '', price)
  return float(numeric_string)
  