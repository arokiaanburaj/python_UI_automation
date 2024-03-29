"""
@author: Arokia Anburaj
@email: arokiaanburaj@gmail.com
@date: 12-Jul-2015
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class CheckboxPageTest(DriverManager):
    def test_checkboxpage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Checkboxes").select_checkbox(2)
