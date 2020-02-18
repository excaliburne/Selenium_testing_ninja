from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class MainPageLocators():
    # Main page locators

    # TOP MENU
    CHECKOUT_BUTTON = (By.XPATH, "//li[5]/a/span")
    CART_BUTTON = (By.XPATH, "//div[@id='cart']/button")
    SHOPPING_CART_BUTTON = (By.XPATH, "//span[contains(.,'Shopping Cart')]")
    WISH_LIST_BUTTON = (By.XPATH, "//a[@id='wishlist-total']/span")
    DROPDOWN_MYACCOUT = (By.XPATH, "//a/span")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Register')]") # Can only be selected if register drop down has been selected previously
    MAIN_LOGO_RETURN_MENU = (By.XPATH, "//a[contains(text(),'The Ninja Store')]")
    CURRENCY_DROPDOWN = (By.XPATH, "//form[@id='form-currency']/div/button/span")

    # BELOW
    ITEM_CLICK = (By.XPATH, "//div[@id='content']/div[2]/div[2]/div/div[2]/h4/a") # Click on any positioned item at place 2
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, '')
    

    SIGNIN_EMAIL_FIELD = (By.XPATH, "")
    SIGNIN_PASSWORD_FIELD = (By.XPATH, "")  
    SIGNUP_EMAIL_FIELD = (By.ID, "")
    SIGNUP_PASSWORD_FIELD = (By.XPATH, "")

