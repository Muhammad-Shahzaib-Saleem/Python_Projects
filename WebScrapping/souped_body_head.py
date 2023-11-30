from bs4 import BeautifulSoup;
import requests;

res = requests.get("https://onout.org/uniswapFork")

soup = BeautifulSoup(res.content,"html.parser");

page_title = soup.title.text

page_body = soup.body
page_head = soup.head


print(page_body,page_head);