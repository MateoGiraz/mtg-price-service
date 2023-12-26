from service.scrapper import scrap
from model.card import Card

def get_prices(card_name, card_edition, session):
  if (card_edition == ""):
    existing_prices = session.query(Card).filter_by(name=card_name).all() 
  else:
    existing_prices = session.query(Card).filter_by(name=card_name, edition=card_edition).all()

  if existing_prices and all(data.is_fresh() for data in existing_prices):
    return existing_prices
    
  prices = scrap(card_name)
  cards = [Card(name, price, edition) for name, price, edition in prices if name == card_name and (edition == card_edition or card_edition == "")]

  session.query(Card).filter_by(name=card_name).delete()

  session.add_all(cards)
  session.commit()
  
  return cards
