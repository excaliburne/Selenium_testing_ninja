import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

print("Test")

class TestAddingiPhoneandcheckingout(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def test_adding_iPhone_and_checking_out(self):
    self.driver.get("http://tutorialsninja.com/demo/")
    self.driver.set_window_size(1680, 1017)
    self.driver.find_element(By.LINK_TEXT, "iPhone").click()
    self.driver.find_element(By.ID, "input-quantity").click()
    self.driver.find_element(By.ID, "input-quantity").send_keys("1")
    time.sleep(1)
    self.driver.find_element(By.ID, "button-cart").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "cart-total").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "strong > .fa-share").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-heading").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Use Coupon Code").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "input-coupon").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "input-coupon").send_keys("345COUPON")
    time.sleep(1)
    self.driver.find_element(By.ID, "button-coupon").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Estimate Shipping & Taxes").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "input-country").click()
    time.sleep(1)
    dropdown = self.driver.find_element(By.ID, "input-country")
    time.sleep(1)
    dropdown.find_element(By.XPATH, "//option[. = 'Estonia']").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "input-zone").click()
    time.sleep(1)
    dropdown = self.driver.find_element(By.ID, "input-zone")
    time.sleep(1)
    dropdown.find_element(By.XPATH, "//option[. = 'Harjumaa (Tallinn)']").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "input-postcode").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "input-postcode").send_keys("10616")
    time.sleep(1)
    self.driver.find_element(By.ID, "button-quote").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".radio > label").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "button-shipping").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".pull-right > .btn").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Continue Shopping").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "search").click()

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()