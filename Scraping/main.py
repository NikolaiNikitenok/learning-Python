import requests, bs4

URL = "https://2ip.ru/"

response = requests.get(URL).text

print(response)
