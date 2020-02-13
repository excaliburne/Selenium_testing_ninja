import unittest
import time
import json
import sys
import pathlib
from random_generator import randomString, randomSimplePassword, randomComplexPassword
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
from locators.locator import RegistrationPage

# generate some ranom info from random_generator.py
firstname = randomString(10)
lastname = randomString(10)
password = randomSimplePassword()
email = randomString(7) + "@emx.com"

class TestRegistrationvalid(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.wait = WebDriverWait(self.driver, 100)
  
  def test_registrationvalid(self):
    driver = self.driver
    self.driver.get("http://tutorialsninja.com/demo/")
    self.driver.set_window_size(1680, 1027) 

    # going to locators/locator.py to opening menu function
    open_menu_register = RegistrationPage(driver)
    open_menu_register.MenuRegister()

    # going to locators/locator.py to go trough registration function
    reg = RegistrationPage(driver)
    reg.Register(firstname, lastname, email, password)
    time.sleep(2)

  def teardown_method(self):
    self.driver.quit()

if __name__ == "__main__":
    unittest.main()