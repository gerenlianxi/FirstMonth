import requests

# 目标：测试网页（安全、公开、允许爬）
url = "https://httpbin.org/get"

# 伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 发送请求
response = requests.get(url, headers=headers)

# 打印结果
print("状态码：", response.status_code)
print("\n网页内容：\n", response.text)