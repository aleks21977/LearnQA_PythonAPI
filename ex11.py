import requests


def test_homework_cookie():
    response = requests.post("https://playground.learnqa.ru/api/homework_cookie")
    print(dict(response.cookies))
    value_cookie = response.cookies["HomeWork"]
    print(value_cookie)
    assert value_cookie == "hw_value", f"Wrong cookie: '{value_cookie}'"

