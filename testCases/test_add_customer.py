import random
import string

from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from pageObjects.login_page import LoginPage
from utilities.customLogger import LogGen
from pageObjects.add_customer_page import AddCustomerPage


class TestAddCustomer:
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen(__name__)

    def test_add_customers(self, setup):
        self.logger.info("TestCase_003_AddCustomer")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.login_pg = LoginPage(self.driver)
        self.login_pg.set_username(self.username)
        self.login_pg.set_password(self.password)
        self.login_pg.click_login_button()
        self.logger.info("Login successfully")
        self.logger.info("adding new customer to the customer page is started...")
        self.driver.set_page_load_timeout(60)
        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_on_customer_menu()
        self.add_customer.click_on_customer_menu_items()
        self.add_customer.click_on_add_customer_button()
        self.email = random_generator()+ "@gmail.com"
        print(self.email)
        self.add_customer.set_email(self.email)
        self.add_customer.set_password(self.password)
        self.add_customer.set_firstname("Spider")
        self.add_customer.set_lastname("Reddy")
        self.add_customer.click_on_gender_radio_btn("Male")
        self.add_customer.set_company_name("Amazon")
        self.add_customer.click_on_tax_checkbox()
        self.add_customer.set_newsletter("nop")
        self.add_customer.set_customer_role("Guests")
        self.add_customer.set_manager_of_vendor(2)
        self.add_customer.click_on_checkbox_activate()
        self.add_customer.click_on_checkbox_change_password()
        self.add_customer.set_admin_comments("This is to test the add customer page")
        self.add_customer.click_on_save_button()
        self.driver.set_page_load_timeout(60)
        self.logger.info("saving customer to the customer page")
        self.logger.info("Add customer validation is starting.....")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("Add customer testcase is passed...")
        else:
            self.driver.save_screenshot("")
            self.logger.error("Add customer testcase is Failed...")
            assert False

        self.driver.close()
        self.logger.info("TestCase_003 is successfully completed")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
