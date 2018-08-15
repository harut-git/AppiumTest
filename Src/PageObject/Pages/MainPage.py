from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators import Locator


class Main(object):
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = None
        self.register_button = None
        self.forgot_password = None
        wait = WebDriverWait(self.driver, 40)
        print wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.reg_login_buttons)))
        self.reg_login_buttons = driver.find_elements(By.CLASS_NAME, Locator.reg_login_buttons)
        for i in self.reg_login_buttons:
            if i.text == "SIGN IN":
                self.sign_in_button = i
            elif i.text == "REGISTER":
                self.register_button = i
            elif i.text == "ENTER AS GUEST":
                self.forgot_password = i
            else:
                print "No Buttons Located!!!!"
