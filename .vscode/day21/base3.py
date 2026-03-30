import requests

url = "https://api.github.com"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
data = res.json()

print("GitHub API 信息：")
print("用户URL：", data["user_url"])