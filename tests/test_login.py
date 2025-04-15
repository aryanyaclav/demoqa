from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    WebDriverWait(driver, 10).until(EC.url_to_be("https://demoqa.com/profile"))

    assert driver.current_url == "https://demoqa.com/profile"