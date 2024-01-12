from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
  The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
  """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def is_element_present(self, locator):
        self.find(*locator).is_displayed()

    def get_current_url_and_check(self, expected_url):
        assert expected_url == self.driver.current_url

    def scroll_to_element(self, locator):
        element = self.find(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_element_web_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_element_web_element_actions(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover_on_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(element))

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def click_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(element))
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    def scroll_to_element_actions(self, locator_or_element):
        if isinstance(locator_or_element, tuple):  # Check if it's a locator
            element = self.find(*locator_or_element)
        elif isinstance(locator_or_element, WebElement):  # Check if it's a WebElement
            element = locator_or_element
        else:
            raise ValueError("Invalid parameter. Provide either a locator or a WebElement.")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def select_element_by_value(self, locator, value):
        element = self.find(*locator)
        select = Select(element)
        select.select_by_value(value)

    def find_elements(self, *locator, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except Exception as e:
            print(f"Error finding elements: {e}")
            return []

    def switch_window(self, element):
        current_window = self.driver.window_handles[0]
        self.click(element)

        # Wait for the new window to open
        WebDriverWait(self.driver, 10).until(lambda driver: len(self.driver.window_handles) > 1)

        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break
