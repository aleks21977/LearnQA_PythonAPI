import requests


def test_homework_headers():
    response = requests.post("https://playground.learnqa.ru/api/homework_header")
    print(response.headers["x-secret-homework-header"])
    value_headers = response.headers["x-secret-homework-header"]
    print(value_headers)
    assert value_headers == "Some secret value", f"Wrong headers: '{value_headers}'"

