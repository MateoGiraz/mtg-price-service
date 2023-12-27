import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import namedtuple

def scrap(name):
  url = "http://www.cardkingdom.com/catalog/view?filter%%5Bipp%%5D=60&filter%%5Bsort%%5D=most_popular&filter%%5Bsearch%%5D=mtg_advanced&filter%%5Bname%%5D=%s&filter%%" % (name)

  results = []

  chrome_options = Options()
  chrome_options.add_argument("--headless")

  dr = webdriver.Chrome(options=chrome_options)
  dr.get(url)

  html_soup = BeautifulSoup(dr.page_source, 'html.parser')

  listing = html_soup.find('div', class_="row productListRow")

  cards = listing.find_all('div', class_="productItemWrapper productCardWrapper")

  for card in cards:
    title = card.find('span', class_="productDetailTitle").text.strip()
    edition = card.find('div', class_="productDetailSet").find("a").text.strip()

    card_prices = card.find_all('span', class_="stylePrice")

    nm_price = getFloat(card_prices[0].text.strip())
    ex_price = getFloat(card_prices[1].text.strip())
    vg_price = getFloat(card_prices[2].text.strip())
    g_price = getFloat(card_prices[3].text.strip())

    results.append((title, {'nm': nm_price, 'ex': ex_price, 'vg': vg_price, 'g': g_price}, getEditionString(edition)))

  dr.quit()
  return results

def getFloat(price):
  numeric_string = re.sub(r'[^\d.]', '', price)
  return float(numeric_string)

def getEditionString(edition):
  return edition.split('\n')[0]