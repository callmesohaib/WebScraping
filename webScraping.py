from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com/")
# page_to_scrape = requests.get("https://www.scrapethissite.com/pages/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})
prices = soup.findAll("p", attrs={"class": "lead session-desc"})


for quote, author in zip(quotes, authors):
    print(quote.text + "\n\t" + author.text)
# for price in prices:
#     print(price.text.lstrip())



