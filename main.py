import requests

data = {"method": "GET"}
data["method"] = "POST"
print(data)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data)
print(response.text)
print(response.status_code)