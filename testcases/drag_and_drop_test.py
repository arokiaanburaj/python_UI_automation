""" 
@author: Arokia Anburaj
@email: arokiaanburajj@gmail.com
@date: 12-Jul-2015
"""
from pages.welcome_page import WelcomePage
from pages.drag_and_drop_page import DragAndDropPage
from utility.drivermanager import DriverManager


class DragAndDropPageTest(DriverManager):
    def test_drag_and_drop_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Drag Drop Test")
        dragAndDropPage = DragAndDropPage(self.driver)
        dragAndDropPage.drag_a_to_b()
        import time
        time.sleep(5)

