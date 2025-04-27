from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.logger = get_logger(self.__class__.__name__)

    def find_element(self, locator):
        self.logger.info(f"Locating element: {locator}")
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        
    
    def click(self, locator):
        self.find_element(locator).click()
        self.logger.info(f"Clicked on element: {locator}")

    def send_keys(self, locator, text):
        self.logger.info(f"Sending text: {text} to element: {locator}")
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")
        return self.find_element(locator).text
    
    def get_title(self):
        self.logger.info("Getting page title")
        return self.driver.title
    
    def open_url(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)
