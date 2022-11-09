import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
count_responses = len(response.history)
print(f"Количество запросов = {count_responses}")
if count_responses > 1:
    print(f"Последний URL - {response.history[(int(count_responses) - 1)].url}")