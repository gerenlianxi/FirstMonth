import requests

url = "https://www.baidu.com/s"
params = {
    "wd": "Python"
}

response = requests.get(url, params=params)
print(response.text)