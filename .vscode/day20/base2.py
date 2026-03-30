import requests

# 访问百度
res = requests.get("https://www.baidu.com")

print("请求成功！状态码：", res.status_code)
print("网页标题：", res.text[:100])  # 只打印前100个字符