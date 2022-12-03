import json.decoder
import string
import random
from datetime import datetime

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot fnd cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot fnd header with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    def prepere_registration_data(self, email=None, maxlen=None):
        name = "learnqa"
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"

        if maxlen is not None:
            name = self.random_string(maxlen)

        return {
            'password': '123',
            'username': f'{name}',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def random_string(self, maxlen=1):
        name = ""
        return name + "".join([random.choice(string.ascii_letters) for i in range(maxlen)])
