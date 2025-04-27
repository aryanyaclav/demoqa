from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from utils.logger import get_logger

class LoginPage(BasePage):
    #Loactors
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "name")
    BOOK_STORE_BUTTON = (By.ID, "gotoStore")

    def __init__(self, driver):
        super().__init__(driver)


    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        loginButton = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(self.LOGIN_BUTTON))

        self.driver.execute_script("arguments[0].click();", loginButton) # this line will click using javascript
        self.logger.info(f"Clicked on login button")

    def wait_for_login_success(self):
        WebDriverWait(self.driver, self.timeout).until(EC.url_contains("profile"))
        self.logger.info("Login successful")

    def get_error_message(self):
        self.logger.info("Getting error message")
        return self.get_text(self.ERROR_MESSAGE)
        
    
    def goto_bookstore(self):
        storeButton = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(self.BOOK_STORE_BUTTON))
        self.driver.execute_script("arguments[0].click();", storeButton)
        self.logger.info(f"Clicked on book store button")