from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    home_page_check_element=(By.XPATH, "//b[text()='Insider Named #1 G2 Leader in Winter’24 Reports']")
    accept_all_button = (By.XPATH, "//*[contains(text(),'Accept All')]")
    careers_button = (By.XPATH, "//a[contains(text(),'Careers')]")
    company_button = (By.XPATH, "//a[contains(text(),'Company')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_accept_all(self):
        self.click(self.accept_all_button)

    def check_if_on_home_page(self,expected_url):
        self.is_element_present(self.home_page_check_element)
        self.get_current_url_and_check(expected_url)

    def navigate_to_careers_from_home_tab(self):
        self.click(self.company_button)
        self.click(self.careers_button)


