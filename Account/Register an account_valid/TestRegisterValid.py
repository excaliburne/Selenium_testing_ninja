import unittest
import time
import json
import sys
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

class TestRegistrationvalid(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.wait = WebDriverWait(self.driver, 100)
  
  def test_registrationvalid(self):
    self.driver.get("http://tutorialsninja.com/demo/")
    self.driver.set_window_size(1680, 1027)
    
    self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".dropdown .hidden-xs")))
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()

    self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),\'Register\')]")))
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Register\')]").click()

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-firstname")))
    self.driver.find_element(By.ID, "input-firstname").click()

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-firstname")))
    self.driver.find_element(By.ID, "input-firstname").send_keys(randomString(10))

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-lastname")))
    self.driver.find_element(By.ID, "input-lastname").click()
    self.driver.find_element(By.ID, "input-lastname").send_keys(randomString(10))

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-email")))
    self.driver.find_element(By.ID, "input-email").click()
    self.driver.find_element(By.ID, "input-email").send_keys("anything@gmail.com")

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-telephone")))
    self.driver.find_element(By.ID, "input-telephone").click()
    self.driver.find_element(By.ID, "input-telephone").send_keys("54534264")

    self.wait.until(EC.element_to_be_clickable((By.ID, "input-password")))
    self.driver.find_element(By.ID, "input-password").click()
    r_pass = randomComplexPassword()
    self.driver.find_element(By.ID, "input-password").send_keys(r_pass)
    self.driver.find_element(By.ID, "input-confirm").click()
    self.driver.find_element(By.ID, "input-confirm").send_keys(r_pass)
    self.driver.find_element(By.NAME, "agree").click()
    time.sleep(1)
    self.driver.find_element(By.XPATH, "//input[@value=\'Continue\']").click()
    time.sleep(1)


  def teardown_method(self):
    self.driver.quit()

if __name__ == "__main__":
    unittest.main()