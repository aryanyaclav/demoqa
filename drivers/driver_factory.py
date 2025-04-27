from selenium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser.lower() == 'chrome':
            driver = webdriver.Chrome()

        elif browser.lower() == 'firefox':            
            driver = webdriver.Firefox()
            
        else:
            raise Exception(f"Browser {browser} is not supported")
        
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        return driver