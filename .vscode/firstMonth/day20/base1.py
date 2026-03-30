import requests

url = "https://api.github.com"
res = requests.get(url)

# 打印JSON数据
data = res.json()
print(data)
print("用户地址:", data["user_url"])