from scrapper import scrap

def get_prices(name):
  #get db price

  #if existing price and TTL not exceeded
    #return existing data
    
  cards = scrap(name)
  #update db price and TTL
  
  return cards
