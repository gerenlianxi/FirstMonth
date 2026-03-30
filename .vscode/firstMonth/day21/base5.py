import requests

# 关键修复：用 https 的完整地址 + 完整请求头
url = "https://www.baidu.com/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers, allow_redirects=True)
res.encoding = "utf-8"  # 确保中文不乱码
html = res.text

# 提取标题
start = html.find("<title>") + 7
end = html.find("</title>")
title = html[start:end]

print("网页标题：", title)