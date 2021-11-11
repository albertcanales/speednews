import requests
from bs4 import BeautifulSoup

URL = input()
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

text = soup.find(id="maincontent")

paragraphs = text.find_all("p")

for paragraph in paragraphs:
	print(paragraph.text, "\n")
