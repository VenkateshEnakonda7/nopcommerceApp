'''Scenarios to test login page'''
from pageObjects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestLogin:
    '''
    created test class
    '''
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    ''' testing home page title'''
    def test_title_homepage(self, setup):
        self.logger.info("**********Test_001_login***********")
        self.logger.info("*******verifying the Home page title********")
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
            self.logger.info("********Home page title is passed********")
        else:
            self.driver.save_screenshot(".//Screenshots//" +
                                        "test_title_homepage.png")
            self.driver.close()
            self.logger.error("********Home page title is failed")
            assert False

    def test_login(self, setup):
        '''testing login functionality as well as title after login'''
        self.logger.info("**********verifying the login functionality*******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.login_pg = LoginPage(self.driver)
        self.login_pg.set_username(self.username)
        self.login_pg.set_password(self.password)
        self.login_pg.click_login_button()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("*******Login page testcase is passed******")
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.close()
            self.logger.error("**********Login testcase is failed*****")
            assert False
