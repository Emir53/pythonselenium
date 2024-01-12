from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CareersQaPage(BasePage):
    see_all_qa_jobs_button = (By.XPATH, "//a[normalize-space()='See all QA jobs']")
    def __init__(self, driver):
        super().__init__(driver)

    def click_all_qa_jobs_button(self):
        self.click(self.see_all_qa_jobs_button)