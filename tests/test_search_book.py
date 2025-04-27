import pytest
from pages.search_page import SearchPage
from pages.login_page import LoginPage


@pytest.mark.parametrize("book_name, expected_result", [
    ("Git Pocket Guide", "Git Pocket Guide"),
    ("Speaking JavaScript", "Speaking JavaScript")
])
def test_search_book(driver, config, book_name, expected_result):
    login_page = LoginPage(driver)
    login_page.open_url(config["base_url"] + "/login")

    username = config["credentials"]["username"]
    password = config["credentials"]["password"]

    login_page.login(username, password)

    login_page.wait_for_login_success()

    login_page.goto_bookstore()

    search_page = SearchPage(driver)
    search_page.search_for_book(book_name)

    search_results = search_page.get_search_results()
    assert expected_result in search_results, f"Expected '{expected_result}' in search results, but got '{search_results}'"
