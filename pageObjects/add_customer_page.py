import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class AddCustomerPage:

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuItems_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addNew_xpath = "//a[@class='btn btn-primary']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstName_xpath = "//input[@id='FirstName']"
    txt_lastName_xpath = "//input[@id='LastName']"
    radio_gender_male_xpath = "//input[@id='Gender_Male']"
    radio_gender_female_xpath = "//input[@id='Gender_Female']"
    txt_companyName_xpath = "//input[@id='Company']"
    checkbox_tax_xpath = "//input[@id='IsTaxExempt']"
    newsletter_xpath = "//span[@class='select2-selection select2-selection--multiple']"
    txt_newsletter_xpath = "//input[@class='select2-search__field']"
    lst_newsletter_id = f"//li[contains(@class,'select2-results__option')]"

    remove_xpath = "//span[@role='presentation']"
    txt_customer_role_xpath = "(//input[@role='searchbox'])[2]"
    lst_customer_role_admin_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-bsu5-1']"
    lst_customer_role_register_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-wwow-3']"
    lst_customer_role_guests_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-0hjw-4']"
    lst_customer_role_vendor_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-mg73-5']"
    lst_customer_role_qa_software_xpath = "//li[@title='QA Software']"
    select_vendor_xpath = "//select[@id='VendorId']"
    checkbox_active_xpath = "//input[@id='Active']"
    checkbox_change_password_xpath = "//input[@id='MustChangePassword']"
    txt_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']//i[@class='far fa-floppy-disk']"


    def __init__(self,driver):
        self.driver = driver

    def click_on_customer_menu(self, timeout:int=10):
        wait = WebDriverWait(self.driver, timeout)
        customer_click = wait.until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menu_xpath)))
        customer_click.click()

    def click_on_customer_menu_items(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuItems_xpath).click()

    def click_on_add_customer_button(self):
        self.driver.find_element(By.XPATH,self.btn_addNew_xpath).click()

    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def set_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstName_xpath).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastName_xpath).send_keys(lastname)

    def click_on_gender_radio_btn(self, gender):
        if gender == "male":
            self.driver.find_element(By.XPATH, self.radio_gender_male_xpath).click()
        elif gender == "female":
            self.driver.find_element(By.XPATH, self.radio_gender_female_xpath).click()

    def set_company_name(self, companyname):
        self.driver.find_element(By.XPATH, self.txt_companyName_xpath).send_keys(companyname)

    def click_on_tax_checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, self.checkbox_tax_xpath)
        if not checkbox.is_selected():
            checkbox.click()

    def set_newsletter(self, newsletter: str, timeout: int = 10) -> bool:
        """
        Selects a value from the Select2 newsletter dropdown.
        Returns True on success, False otherwise.
        """
        self.driver.execute_script("window.scrollTo(0, 1000);")  # Scrolls to vertical position 1000
        wait = WebDriverWait(self.driver, timeout)

        # 1) Click the Select2 box to activate it
        dropdown_toggle = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.newsletter_xpath))
        )
        dropdown_toggle.click()

        # 2) Type into the search input inside the dropdown
        search_box = wait.until(
            EC.presence_of_element_located((By.XPATH, self.txt_newsletter_xpath))
        )
        search_box.send_keys(newsletter)

        # 3) Wait for the matching option to appear in results list
        result_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lst_newsletter_id)))
        result_option.click()
        return True

    def set_customer_role(self, role: str, timeout: int = 15) -> bool:
        """
        Selects a customer role from the Select2 dropdown.
        Works for multi-select widgets like Customer Roles.
        """
        wait = WebDriverWait(self.driver, timeout)
        dropdown_text_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']")))
        dropdown_text_box.click()

        dropdown_toggle = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@role='searchbox'])[2]")))

        dropdown_toggle.send_keys(role)

        options = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//ul[@id='select2-SelectedCustomerRoleIds-results'])[1]"))
        )
        options.click()
        time.sleep(5)


    def set_manager_of_vendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.select_vendor_xpath))
        drp.select_by_index(value)

    def click_on_checkbox_activate(self):
        checkbox = self.driver.find_element(By.XPATH, self.checkbox_tax_xpath)
        if not checkbox.is_selected():
            checkbox.click()

    def click_on_checkbox_change_password(self):
        checkbox = self.driver.find_element(By.XPATH, self.checkbox_change_password_xpath)
        if not checkbox.is_selected():
            checkbox.click()

    def set_admin_comments(self, comment):
        self.driver.find_element(By.XPATH, self.txt_admin_comment_xpath).send_keys(comment)

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
