from bs4 import BeautifulSoup;
import requests;


res = requests.get("https://onout.org/uniswapFork")

soup = BeautifulSoup(res.content,"html.parser");

first_h1 = soup.select(h2)[0].text

print(first_h1)