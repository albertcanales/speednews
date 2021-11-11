import requests
from bs4 import BeautifulSoup

URL = input()
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

headlines = soup.find(id="headlines")

headers = headlines.find_all(class_="fc-item__container")

for header in headers:
	title = header.find(class_="u-faux-block-link__overlay js-headline-text")
	print(title["href"], title.text)
