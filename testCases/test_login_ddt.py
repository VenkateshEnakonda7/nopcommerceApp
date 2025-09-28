'''Scenarios to test login page'''
from pageObjects.login_page import LoginPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLoginDDT:
    '''
    created test class
    '''
    baseUrl = ReadConfig.get_application_url()
    path = ".//TestData/logindata.xlsx"
    logger = LogGen.loggen(__name__)

    ''' testing home page title'''
    def test_title_homepage(self, setup):
        self.logger.info("**********Test_002_login_data_driven_test***********")
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

    def test_login_ddt(self, setup):
        '''testing login functionality as well as title after login'''
        self.logger.info("**********verifying the login functionality*******")
        self.driver = setup
        self.login_pg = LoginPage(self.driver)
        self.rows=XLUtils.get_row_count(self.path,'Sheet1')
        for row in range(2,self.rows+1):
            self.driver.get(self.baseUrl)
            self.username = XLUtils.read_data(self.path,'Sheet1',row,1)
            self.password = XLUtils.read_data(self.path,'Sheet1',row,2)
            self.exp = XLUtils.read_data(self.path,'Sheet1',row,3)
            self.login_pg.set_username(self.username)
            self.login_pg.set_password(self.password)
            self.login_pg.click_login_button()

        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"
        lst_status = []

        if actual_title == expected_title:
            self.logger.info("*******Login page testcase is passed******")
            if self.exp == "pass":
                self.logger.info("Expected testcase is Passed")
                self.login_pg.click_logout_button()
                lst_status.append("Pass")
            elif self.exp == 'fail':
                self.logger.info('Expected testcase is filed')
                self.login_pg.click_logout_button()
                lst_status.append("Fail")
        elif actual_title != expected_title:
            if self.exp == "pass":
                self.logger.info("Expected testcase is Passed")
                self.login_pg.click_logout_button()
                lst_status.append("Pass")
            elif self.exp == 'fail':
                self.logger.info('Expected testcase is filed')
                self.login_pg.click_logout_button()
                lst_status.append("Fail")

        if "Fail" not in lst_status:
            self.logger.info("Data driven test for login testcase is passed")
            self.driver.close()
            assert True
        else:
            self.logger.error("Data driven test for login testcase is failed")
            self.driver.close()
            assert False
