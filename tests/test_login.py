# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest

# def test_valid_login(driver, config):
#     login_page = LoginPage(driver)
#     login_page.open_url(config["base_url"] + "/login")

#     username = config["credentials"]["username"]
#     password = config["credentials"]["password"]

#     login_page.login(username, password)

#     login_page.wait_for_login_success()

#     # Simple validation after login
#     assert "profile" in driver.current_url.lower()


#------------------Negative Test ------------------

# @pytest.mark.parametrize("username,password,expected_error", [
#     ("correct_username", "wrong_password", "Invalid username or password!"),
#     ("wrong_username", "correct_password", "Invalid username or password!"),
#     ("wrong_username", "wrong_password", "Invalid username or password!")
# ])
# def test_invalid_login(driver, config, username, password, expected_error):
#     login_page = LoginPage(driver)
#     login_page.open_url(config["base_url"] + "/login")

#     if username == "correct_username":
#         username = config["credentials"]["username"]
#     if password == "correct_password":
#         password = config["credentials"]["password"]

#     login_page.login(username, password)

#     # Simple validation after login
#     error_message = login_page.get_error_message()
#     assert expected_error in error_message

class TestLogin(BaseTest):
    def test_valid_login(self, driver, config):
        login_page = LoginPage(driver)
        login_page.open_url(config["base_url"] + "/login")

        username = config["credentials"]["username"]
        password = config["credentials"]["password"]

        login_page.login(username, password)

        login_page.wait_for_login_success()

        # Simple validation after login
        assert "profile" in driver.current_url.lower()

    @pytest.mark.parametrize("username,password,expected_error", [
        ("correct_username", "wrong_password", "Invalid username or password!"),
        ("wrong_username", "correct_password", "Invalid username or password!"),
        ("wrong_username", "wrong_password", "Invalid username or password!")
    ])
    def test_invalid_login(self, driver, config, username, password, expected_error):
        login_page = LoginPage(driver)
        login_page.open_url(config["base_url"] + "/login")

        if username == "correct_username":
            username = config["credentials"]["username"]
        if password == "correct_password":
            password = config["credentials"]["password"]

        login_page.login(username, password)

        # Simple validation after login
        error_message = login_page.get_error_message()
        assert expected_error in error_message