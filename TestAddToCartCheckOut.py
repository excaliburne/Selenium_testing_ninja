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
from locators.locator import AddProductToCartCheckout


class TestAddingiPhoneCheckingOut(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Chrome()
      self.vars = {}
      self.wait = WebDriverWait(self.driver, 100)

    def test_adding_iPhone_and_checking_out(self):
      driver = self.driver
      self.driver.get("http://tutorialsninja.com/demo/")
      self.driver.set_window_size(1680, 1017)

      #going to locators/locator.py to AddToCart function
      add_to_cart = AddProductToCartCheckout(driver)
      add_to_cart.AddToCart()

      #going to locators and find Checkout function
      check = AddProductToCartCheckout(driver)
      check.CheckOut()
      time.sleep(2)

    def teardown_method(self):
          self.driver.quit()

if __name__ == "__main__":
    unittest.main()