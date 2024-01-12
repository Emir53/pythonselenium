from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CareersPage(BasePage):
    see_all_teams_button=(By.XPATH, "//a[contains(text(),'See all teams')]")
    location_bar=(By.CSS_SELECTOR, "#location-slider")
    life_at_insider=(By.CSS_SELECTOR, "div.elementor-main-swiper.swiper-container")
    def __init__(self,driver):
        super().__init__(driver)

    def check_all_teams_visible(self):
       self.scroll_to_element(self.see_all_teams_button)
       self.is_element_present(self.see_all_teams_button)
    def check_location_bar(self):
       self.scroll_to_element(self.location_bar)
       self.is_element_present(self.location_bar)
    def check_life_at_insider(self):
        self.scroll_to_element(self.life_at_insider)
        self.is_element_present(self.life_at_insider)
    def navigate_to_qa_careers_page(self):
       self.driver.get("https://useinsider.com/careers/quality-assurance/")



