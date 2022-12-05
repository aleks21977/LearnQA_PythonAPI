import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):

    @allure.feature('feature_2')
    @allure.story('story_2')
    def test_create_user_successfully(self):
        data = self.prepere_registration_data()

        response = MyRequests.post("/user/", data=data)
        print(response.text)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
    @allure.testcase(TEST_CASE_LINK, 'Test case title')
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepere_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_email_without_at(self):
        email = 'vinkotovexample.com'
        data = self.prepere_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        print(response.text)
        assert response.content.decode("utf-8") == "Invalid email format", \
            f"Unexpected response content {response.content}"

    data = [
        {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'},
        {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': "test@email.com"},
        {'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': "test@email.com"},
        {'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': "test@email.com"},
        {'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': "test@email.com"},
    ]

    @allure.issue('140', 'Pytest-flaky test retries shows like test steps')
    @pytest.mark.parametrize("data",  data)
    def test_create_user_without_value(self, data):
        response = MyRequests.post("/user/", data=data)

        contain_text = "The following required params are missed: "
        current_text = response.text

        assert contain_text in current_text, f"{current_text}"
        print(response.text)

    @allure.title("This title will be replaced in a test body")
    def test_create_user_with_name_one_character_long(self):
        data = self.prepere_registration_data(maxlen=1)
        response = MyRequests.post("/user/", data=data)

        expected_massage = "The value of 'username' field is too short"
        assert response.text == expected_massage, f"Incorrect answer: '{response.text}'."

    @allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
    def test_create_user_with_too_long_name(self):
        data = self.prepere_registration_data(maxlen=300)
        response = MyRequests.post("/user/", data=data)

        expected_massage = "The value of 'username' field is too long"
        assert response.text == expected_massage, f"Incorrect answer: '{response.text}'."
