import requests

url = "https://httpbin.org/get"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)

# 保存到 page.html
with open("page.html", "w", encoding="utf-8") as f:
    f.write(res.text)

print("网页已保存到 page.html")