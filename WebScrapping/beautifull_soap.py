from bs4 import BeautifulSoup;
import requests;

page = requests.get("https://onout.org/uniswapFork")

soup = BeautifulSoup(page.content,"html.parser")

title = soup.title.text

print(title)

