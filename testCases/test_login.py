import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class TestLogin:
    baseUrl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"

    def test_title_homepage(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title

        if actual_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_title_homepage.png")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginPg = LoginPage(self.driver)
        self.loginPg.setusername(self.username)
        self.loginPg.setpassword(self.password)
        self.loginPg.click_login_button()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.close()
            assert False

