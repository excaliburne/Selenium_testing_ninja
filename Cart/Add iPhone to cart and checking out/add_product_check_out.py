import unittest
import time
import json
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


print("Test")

class TestAddingiPhoneandcheckingout(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.wait = WebDriverWait(self.driver, 100)

  def test_adding_iPhone_and_checking_out(self):
    self.driver.get("http://tutorialsninja.com/demo/")
    self.driver.set_window_size(1680, 1017)
    self.driver.find_element(By.LINK_TEXT, "iPhone").click()
    self.driver.find_element(By.ID, "input-quantity").click()
    self.driver.find_element(By.ID, "input-quantity").clear()
    self.driver.find_element(By.ID, "input-quantity").send_keys("2")

    self.wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    self.driver.find_element(By.ID, "button-cart").click()

    self.wait.until(EC.element_to_be_clickable((By.ID, "cart-total")))
    self.driver.find_element(By.ID, "cart-total").click()

    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "strong > .fa-share")))
    self.driver.find_element(By.CSS_SELECTOR, "strong > .fa-share").click()

    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-heading")))
    self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-heading").click()

    self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Use Coupon Code")))
    self.driver.find_element(By.LINK_TEXT, "Use Coupon Code").click()

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-coupon")))
    self.driver.find_element(By.ID, "input-coupon").click()

    self.driver.find_element(By.ID, "input-coupon").send_keys("345COUPON")

    self.wait.until(EC.element_to_be_clickable((By.ID, "button-coupon")))
    self.driver.find_element(By.ID, "button-coupon").click()

    self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Estimate Shipping & Taxes")))
    self.driver.find_element(By.LINK_TEXT, "Estimate Shipping & Taxes").click()

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-country")))
    self.driver.find_element(By.ID, "input-country").click()

    dropdown = self.driver.find_element(By.ID, "input-country")
    self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'Estonia']")))
    dropdown.find_element(By.XPATH, "//option[. = 'Estonia']").click()

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-zone")))
    self.driver.find_element(By.ID, "input-zone").click()

    dropdown = self.driver.find_element(By.ID, "input-zone")
    self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'Harjumaa (Tallinn)']")))
    dropdown.find_element(By.XPATH, "//option[. = 'Harjumaa (Tallinn)']").click()

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-postcode")))
    self.driver.find_element(By.ID, "input-postcode").click()
    self.driver.find_element(By.ID, "input-postcode").send_keys("10616")

    self.wait.until(EC.element_to_be_clickable((By.ID, "button-quote")))
    self.driver.find_element(By.ID, "button-quote").click()

    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".radio > label")))
    self.driver.find_element(By.CSS_SELECTOR, ".radio > label").click()
    
    self.wait.until(EC.element_to_be_clickable((By.ID, "button-shipping")))
    self.driver.find_element(By.ID, "button-shipping").click()

    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pull-right > .btn")))
    self.driver.find_element(By.CSS_SELECTOR, ".pull-right > .btn").click()

    self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue Shopping")))
    self.driver.find_element(By.LINK_TEXT, "Continue Shopping").click()

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()