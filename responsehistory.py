import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
count_responses = len(response.history)
print(f"Количество редиректов = {count_responses}")
print(f"Последний URL - {response.url}")
