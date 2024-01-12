import random
from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OpenPositions(BasePage):
    location_closer_button = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
    location_closer_arrow= (By.XPATH, "(//span[@role='presentation'])[1]")
    location_select_element= (By.XPATH, "//li[text()='Istanbul, Turkey']")
    positions_locator = (By.CLASS_NAME, "position-list-item-wrapper")
    view_role_buttons = (By.CSS_SELECTOR, "div#jobs-list>div>div>a")


    #department_dropdown= (By.CSS_SELECTOR, "#select2-filter-by-department-container")

    def __init__(self, driver):
        super().__init__(driver)



    def select_location(self):
        sleep(3)
        self.click(self.location_closer_button)
        sleep(3)
        self.click(self.location_select_element)
        sleep(3)



    def check_positions(self):
        sleep(4)
        positions = self.find_elements(*OpenPositions.positions_locator)
        count = len(positions)
        random_index = random.randint(0, count - 1)
        element = positions[random_index]
        print(element.text)

        for position in positions:
            text = position.text
            parts = text.split("\n")
            position_of_job = parts[0].strip()
            department_of_job = parts[1].strip()
            print(department_of_job)
            location_of_job = parts[2].strip()

            assert "Quality Assurance" in position_of_job or "QA" in position_of_job
            assert "Quality Assurance" in department_of_job
            assert "Istanbul, Turkey" in location_of_job
        self.hover_on_element(element)
        self.click_element(self.view_role_buttons[random_index])









