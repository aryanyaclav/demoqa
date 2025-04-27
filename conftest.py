
import pytest
from drivers.driver_factory import DriverFactory
import yaml
import os

@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path) as file:
        data = yaml.safe_load(file)
    return data

@pytest.fixture(scope="function")
def driver(config):
    browser = config.get("browser", "chrome")
    driver = DriverFactory.get_driver(browser)
    yield driver
    driver.quit()
