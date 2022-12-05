from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):

    def test_delete_user_with_id_2(self):

        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE
        response2 = MyRequests.delete(
            "/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        print(response2.status_code)
        print(response2.text)
        response_text = response2.text

        assert response_text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.",\
            f"Incorrect massage: '{response_text}'"


    def test_delete_with_new_register_user(self):
        # REGISTER
        register_data = self.prepere_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET
        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response3.text)

        # DELETE
        response4 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        print(response4.status_code)
        print(response4.text)

        # GET
        response5 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response5.text)
        response_text = response5.text

        assert response_text == "User not found", f"Incorrect massage: '{response_text}'"


    def test_delete_anothe_user(self):
        # REGISTER
        register_data = self.prepere_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET
        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response3.text)

        # DELETE
        response4 = MyRequests.delete(
            f"/user/53613",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        print(response4.status_code)
        print(response4.text)

        # GET
        response5 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response5.text)
        response_text = response5.text

        assert response_text == "User not found", f"Incorrect massage: '{response_text}'"

