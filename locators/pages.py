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

class AddProductToCartCheckout():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 100)     

    def AddToCart(self):
        # Fills quantity and "add to cart"
        self.driver.find_element(By.LINK_TEXT, "iPhone").click()
        self.driver.find_element(By.ID, "input-quantity").click()
        self.driver.find_element(By.ID, "input-quantity").clear()
        self.driver.find_element(By.ID, "input-quantity").send_keys("2")

    def CheckOut(self):
        # Fills registration form
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

