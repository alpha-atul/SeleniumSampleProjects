from time import sleep
import unittest
from selenium import webdriver
from SampleProjects.POMProjectDemo.Pages.login_page import LoginPage
from SampleProjects.POMProjectDemo.Pages.home_page import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_01_login_validation(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_button()
        sleep(2)
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

    def test_02_valid_username(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_button()
        msg = login.invalid_username()
        self.assertEqual(msg, "Invalid credentials")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/atul.singh/PycharmProjects/SeleniumSampleProjects/SampleProjects/Reports"))