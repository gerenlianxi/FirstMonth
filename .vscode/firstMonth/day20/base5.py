import requests

# 1. 发送 GET 请求（拿数据）
url = "https://api.github.com"
response = requests.get(url)

# 2. 状态码 200 = 成功
print("状态码:", response.status_code)

# 3. JSON → 转字典
data = response.json()

# 4. 读取数据
print("用户API地址:", data["user_url"])