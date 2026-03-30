import requests  # 导入库

# 1. 发送请求
url = "https://www.baidu.com"
response = requests.get(url)

# 2. 查看状态码
print("状态码:", response.status_code)

# 3. 查看网页内容
print("网页内容:\n", response.text)