import requests
from PIL import Image
from io import BytesIO

# 换一个 100% 能下载的公开图片（无防盗链）
url = "https://picsum.photos/200/200"

# 伪装浏览器（必须加）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# 下载
response = requests.get(url, headers=headers)

# 打开图片
img = Image.open(BytesIO(response.content))

# 保存成 JPG
img.convert("RGB").save("result.jpg", "JPEG")
print("已保存：result.jpg")

# 保存成 GIF
img.save("result.gif", "GIF")
print("已保存：result.gif")