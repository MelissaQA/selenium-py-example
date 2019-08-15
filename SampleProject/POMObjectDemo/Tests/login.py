from selenium import webdriver
import time
import unittest
#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from ..Pages.homePage import HomePage
from ..Pages.loginPage import LoginPage
import HtmlTestRunner

#Example from the Selenium with Page Object Model tutorial on https://youtu.be/BURK7wMcCwU

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Select the required driver for the browser to use
        cls.driver = webdriver.Chrome(executable_path='POMObjectDemo/Tests/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(3)


    def test_02_login_invalid(self):
        driver = self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()

        message = login.check_invalid_username_message()
        print message
        self.assertEquals(message, "Invalid credentials")

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed!")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))