from json.decoder import JSONDecodeError
import requests
import time


URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

def responsejson():
    global parsed_response_text
    try:
        parsed_response_text = response.json()
    except JSONDecodeError:
        print("Response is not a JSON format")

response = requests.get(URL)
# print(response.text)
responsejson()
token = (parsed_response_text["token"])
params = {"token": f"{token}"}
time_sleep = (parsed_response_text["seconds"])

response = requests.get(URL, params=params)
# print(response.text)
responsejson()
status = (parsed_response_text["status"])

if status == "Job is NOT ready":
    print('Проверка выполнения задачи, получен коректный статус - "' +status+ '"')
else:
    print('Проверка выполнения задачи, получен некоректный статус - "' +status+ '"')

time.sleep(time_sleep)
response = requests.get(URL, params=params)
# print(response.text)
responsejson()
status = (parsed_response_text["status"])
if status == "Job is ready":
    print('Проверка завершения выполнения задачи, получен коректный статус - "' +status+ '"')
else:
    print('Проверка завершения выполнения задачи, получен некоректный статус - "' +status+ '"')

if "result" in parsed_response_text:
    print('поле result в json ответа есть')
else:
    print('поле result в json ответа отсутствует!')