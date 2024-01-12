from time import sleep

import pytest

from pages.careers_page import CareersPage
from pages.careers_qa_page import CareersQaPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.open_positions import OpenPositions
from testCases.base_test import BaseTest


class TestLogin(BaseTest):

    def test_valid_credits(self):
      home_page = HomePage(self.driver)
      login_page=LoginPage(self.driver)

      login_page.login_with_email_and_password("emir","makas")


    def test_invalid_credits(self):
        home_page = HomePage(self.driver)
        careers_page = CareersPage(self.driver)
        careers_qa_page = CareersQaPage(self.driver)
        open_positions=OpenPositions(self.driver)
        home_page.click_accept_all()
        home_page.check_if_on_home_page("https://useinsider.com/")
        home_page.navigate_to_careers_from_home_tab()
        careers_page.check_all_teams_visible()
        careers_page.check_location_bar()
        careers_page.check_life_at_insider()
        careers_page.navigate_to_qa_careers_page()
        careers_qa_page.click_all_qa_jobs_button()
        open_positions.select_location()
        open_positions.check_positions()




