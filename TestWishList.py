import unittest
import time
import json
import sys
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Testwish(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 100)
  
    def test_access_wish(self):
        wish_button = "#wishlist-total > .hidden-xs"

        self.driver.get("http://tutorialsninja.com/demo/")
        self.driver.set_window_size(1920, 1177)
        self.driver.find_element(By.CSS_SELECTOR, wish_button).click()
        time.sleep(2)


    def teardown_method(self, method):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()