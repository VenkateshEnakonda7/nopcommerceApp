'''Scenarios to test login page'''
from pageObjects.login_page import LoginPage


class TestLogin:
    '''
    created test class
    '''
    baseUrl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    ''' testing home page title'''
    def test_title_homepage(self, setup):
        '''

        :type setup: object
        :param setup:
        :return: true/false
        '''
        self.driver = setup
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title

        if actual_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" +
                                        "test_title_homepage.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        '''testing login functionality as well as title after login'''
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.login_pg = LoginPage(self.driver)
        self.login_pg.setusername(self.username)
        self.login_pg.setpassword(self.password)
        self.login_pg.click_login_button()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.close()
            assert False
