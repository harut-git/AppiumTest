import unittest
from appium import webdriver
import time
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Src.PageObject.Pages.MainPage import Main


class AndroidSportsbook(unittest.TestCase):
    "Class to run tests against the ATP WTA app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps.setdefault("autoGrantPermissions", "true")
        desired_caps.setdefault("autoAcceptAlerts", "true")
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = '$ Your device name'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'com.betconstruct.sportsbook'
        desired_caps['appActivity'] = 'com.betconstruct.sportsbook.MainActivityVbet'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_login(self):
        self.driver.implicitly_wait(10)
        main = Main(self.driver)
        time.sleep(2)
        main.sign_in_button.click()
        reg_buttons = self.driver.find_elements_by_class_name("android.widget.MultiAutoCompleteTextView")
        for j in reg_buttons:
            if j.text == 'Username':
                j.send_keys("test88test")
            elif j.text == 'Password':
                j.send_keys("Test123456")
        main.sign_in_button.click()


# ---START OF SCRIPT


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=''))
