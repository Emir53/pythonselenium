from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    email_field = (By.XPATH, "//input[@data-qa='login-email']")
    password_field = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")


    def __init__(self, driver):
        super().__init__(driver)

    def login_with_email_and_password(self, email, password):
        self.set(self.email_field, email)
        self.set(self.password_field,password)
        self.click(self.login_button)
