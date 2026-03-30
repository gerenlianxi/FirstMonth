import requests

url = "https://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
print(res.text[:500])  # 只打印前500字符