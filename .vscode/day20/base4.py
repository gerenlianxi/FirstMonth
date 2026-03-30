import requests

img_url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d5572076ee.png"
res = requests.get(img_url)

# 保存图片
with open("logo.png", "wb") as f:
    f.write(res.content)