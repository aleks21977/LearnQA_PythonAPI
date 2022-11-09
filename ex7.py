import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1. " +response.text)

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print("2. " +response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print("3. " +response.text)


params = {"method": "GET"}


def print_result(methods, response):
    print("С методом " + methods + " текст ответа такой - " + response.text)
    print("код ответа -" + str(response.status_code))


def getparams(methods):
    params["method"] = f"{methods}"

URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

print("4. ")
for methods in "GET", "POST", "PUT", "DELETE":
    print("Проверяем параметр:" +methods)
    getparams(methods)
    response = requests.get(URL, params=params)
    print_result("GET", response)
    getparams(methods)
    response = requests.post(URL, data=params)
    print_result("POST", response)
    getparams(methods)
    response = requests.put(URL, data=params)
    print_result("PUT", response)
    getparams(methods)
    response = requests.delete(URL, data=params)
    print_result("DELETE", response)
    print()
