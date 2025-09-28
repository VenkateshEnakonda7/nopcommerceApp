from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.login_page import LoginPage
from pageObjects.add_customer_page import AddCustomerPage
from pageObjects.search_customer_page import SearchCustomer

class TestCustomer:
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    first_name = "Brenda"
    name = "Brenda Lindgren"

    def test_search_customer_by_name(self,setup):
        self.logger.info("Logging In to the nop ecommerce customers page")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.login_pg = LoginPage(self.driver)
        self.login_pg.set_username(self.username)
        self.login_pg.set_password(self.password)
        self.login_pg.click_login_button()

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.click_on_customer_menu()
        self.addcust.click_on_customer_menu_items()

        searchcust = SearchCustomer(self.driver)
        searchcust.set_first_name(self.first_name)
        searchcust.click_on_search_button()
        print(searchcust.search_result_count())
        status = searchcust.search_customer_by_name(self.name)
        assert True == status
        self.logger.info("testcase of search customer by name is passed")
        if searchcust.search_result_count()>= 1:
            if status == True and searchcust.search_result_count()>=1:
                assert True
                self.logger.info("Expected name found in the table")
            else:
                self.logger.error("Expected name is not found in the table")
                assert False
        else:
            self.logger.error("Expected name is not in table list")
            assert False







