""" 
@author: Arokia Anburaj
@email: arokiaanburaj@gmail.com
@date: 12-Jul-2015
"""

import logging
import unittest

from selenium import webdriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
import sys, os


class DriverManager(unittest.TestCase):
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self):
        """
        This method is to instantiate the web driver instance.
        """
        logging.info("## SETUP METHOD ##")
        logging.info("# Initializing the webdriver.")
        #self.ffprofile = self.create_ffprofile("C:\\Users\\dell\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\xjncngoo.seleniumProfile")
        #self.driver = webdriver.Firefox(self.ffprofile)
        self.driver = webdriver.Chrome(executable_path="D:\\webdrivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("file:///D:/sahitest/Sahi%20Tests.htm")

    def tearDown(self):
        """
        This is teardown method.
        It is to capture the screenshots for failed test cases,
        & to remove web driver object.
        """
        logging.info("## TEARDOWN METHOD ##")

        if sys.exc_info()[0]:
            logging.info("# Taking screenshot.")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)

        if self.driver is not None:
            logging.info("# Removing the webdriver.")
            self.driver.quit()

    def create_ffprofile(self):
        """
        This function is to create firefox profile.
        :return: firefox profile.
        """
        logging.info("# Setting up firefox profile.")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', os.getcwd())
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                               'text/csv,application/octet-stream,application/pdf,application/vnd.ms-excel')
        profile.set_preference("pdfjs.disabled", True)

        return profile


if __name__ == '__main__':
    unittest.main()
