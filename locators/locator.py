### locators soon to be implemented
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class RegistrationPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 100)

    def MenuRegister(self):
        # simply opens the drop menu and select "Register"
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".dropdown .hidden-xs")))
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),\'Register\')]")))
        self.driver.find_element(By.XPATH, "//a[contains(text(),\'Register\')]").click()
    
    def Register(self, firstname, lastname, email, password):
        # fills the registration form
        self.wait.until(EC.element_to_be_clickable((By.ID, "input-firstname")))
        self.driver.find_element(By.ID, "input-firstname").click()

        self.wait.until(EC.element_to_be_clickable((By.ID, "input-firstname")))
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)

        self.wait.until(EC.element_to_be_clickable((By.ID, "input-lastname")))
        self.driver.find_element(By.ID, "input-lastname").click()
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)

        self.wait.until(EC.element_to_be_clickable((By.ID, "input-email")))
        self.driver.find_element(By.ID, "input-email").click()
        self.driver.find_element(By.ID, "input-email").send_keys(email)

        self.wait.until(EC.element_to_be_clickable((By.ID, "input-telephone")))
        self.driver.find_element(By.ID, "input-telephone").click()
        self.driver.find_element(By.ID, "input-telephone").send_keys("54534264")

        self.wait.until(EC.element_to_be_clickable((By.ID, "input-password")))
        self.driver.find_element(By.ID, "input-password").click()
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.ID, "input-confirm").click()
        self.driver.find_element(By.ID, "input-confirm").send_keys(password)
        self.driver.find_element(By.NAME, "agree").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@value=\'Continue\']").click()
        time.sleep(1)





    
