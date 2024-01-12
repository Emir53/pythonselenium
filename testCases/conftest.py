import pytest
from selenium import webdriver


@pytest.fixture()
def initialize_driver(request):

    driver = webdriver.Chrome()

    request.cls.driver = driver

    driver.get("https://useinsider.com/")
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()