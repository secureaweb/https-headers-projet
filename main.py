import requests

url = "https://secureaweb.fr"

response = requests.get(url)
headers = response.headers

print("URL :", url)

for key, value in headers.items():
    print(key, ":", value)
