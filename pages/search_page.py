from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.SEARCH_BOX = (By.ID, "searchBox")
        self.SEARCH_BUTTON = (By.ID, "basic-addon2")
        self.SEARCH_RESULT = (By.CLASS_NAME, "rt-tbody")

    def search_for_book(self, book_name):
        search_input = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_input.clear()
        search_input.send_keys(book_name)
        self.click(self.SEARCH_BUTTON)

        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(self.SEARCH_RESULT))

    def get_search_results(self):
        search_result = self.find_element(self.SEARCH_RESULT)
        return search_result.text
    