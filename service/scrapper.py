import sys
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
    price = card.find('span', class_="stylePrice").text.strip()

    results.append((title, price))

  dr.quit()
  return results