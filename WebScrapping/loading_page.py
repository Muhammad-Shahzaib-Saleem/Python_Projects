import requests

res = requests.get("https://onout.org/uniswapFork")

print(res.text)
print(res.status_code)