"""
@author: Arokia Anburaj
@email: arokiaanburaj@gmail.com
@date: 12-Jul-2015
"""
from pages.frames_page import FramesPage
from pages.multiple_window_page import MultipleWindowsPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class FramesTest(DriverManager):
    def test_frames(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Frames Test")

        frames = FramesPage(self.driver)
        frames.verify_multiple_windows_page()
        frames.click_on_link("Nested Frames")
        frames.verify_next_frame_txt()
