from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get("https://demoqa.com/login")

    def login(self, username, password):
        self.driver.find_element(By.ID, "userName").send_keys(username)
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.ID,"login").click()