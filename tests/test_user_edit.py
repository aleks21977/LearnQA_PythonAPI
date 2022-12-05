from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
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


        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )


    def test_edit2_just_created_user_without_autorise(self):
        # REGISTER
        register_data = self.prepere_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            data={"firstName": new_name}
        )

        print(response3.text)
        response_text = response3.text

        assert response_text == "Auth token not supplied", f"Incorrect massage: '{response_text}'"


    def test_edit_anothe_user_just_created_user(self):
        # REGISTER
        register_data = self.prepere_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        print(response1.text)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN anothe_user
        login_data = {
            'email': 'learnqa12042022165017@example.com',
            'password': '123'
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id2 = self.get_json_value(response2, "user_id")
        print(response2.text)

        # GET
        response6 = MyRequests.get(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response6.text)

        # EDIT - запрос на редактирование отрабатывает корректно с любым id в том числе и без него
        new_name = "ChangedName113"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )


        # GET
        response7 = MyRequests.get(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(user_id2)
        print(response7.text)

        Assertions.assert_code_status(response3, 200)

        # LOGIN just_created_user
        login_data = {
            'email': email,
            'password': password
        }
        response4 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response4, "auth_sid")
        token = self.get_header(response4, "x-csrf-token")

        # GET
        response5 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        print(response5.text)

        Assertions.assert_json_value_by_name(
            response5,
            "firstName",
            "learnqa",
            "Wrong name of the user after edit"
        )



    def test_edit3_just_created_user_with_email_without_at(self):
        # REGISTER
        email = 'vinkotovexample.com'
        register_data = self.prepere_registration_data(email)
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 400)
        # Assertions.assert_json_has_key(response1, "id")

        print(response1.text)
        response_text = response1.text

        assert response_text == "Invalid email format", f"Incorrect massage: '{response_text}'"

    def test_edit4_just_created_user_with_name_one_character_longt(self):
        # REGISTER
        register_data = self.prepere_registration_data(maxlen=1)
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 400)

        print(response1.text)
        response_text = response1.text

        assert response_text == "The value of 'username' field is too short", f"Incorrect massage: '{response_text}'"