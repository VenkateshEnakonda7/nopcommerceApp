from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchCustomer:
    searchTabXpath = "//div[@class='row search-row']"
    searchEmailXpath = "//input[@id='SearchEmail']"
    searchFirstNameXpath = "//input[@id='SearchFirstName']"
    searchLastNameXpath = "//input[@id='SearchLastName']"
    searchButtonXpath = "//button[@id='search-customers']"
    searchResult = "//table[@id='customers-grid']"
    tableXpath = "(//table[@id='customers-grid'])[1]"
    tableRowXpath = "(//table[@id='customers-grid'])[1]//tbody//tr"
    tableColXpath = "(//table[@id='customers-grid'])[1]//tbody//tr//td"

    def __init__(self,driver):
        self.driver = driver

    def set_email(self, email_id):
        # self.driver.find_element(By.XPATH, self.searchTabXpath).click()
        self.driver.find_element(By.XPATH, self.searchEmailXpath).send_keys(email_id)

    def set_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.searchFirstNameXpath).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.searchLastNameXpath).send_keys(last_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.searchButtonXpath).click()

    def search_result_count(self, timeout:int= 10):
        wait = WebDriverWait(self.driver, timeout)
        count = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.searchResult)))
        return len(count)

    def get_no_of_rows(self, timeout:int = 10):
        wait = WebDriverWait(self.driver, timeout)
        lst = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.tableRowXpath)))
        return len(lst)

    def search_customer_by_email_id(self, email):
        flag = False
        for r in range(1, self.get_no_of_rows()+1):
            table = self.driver.find_element(By.XPATH, self.tableXpath)
            email_id = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[2]").text
            if email_id == email:
                flag = True
        return flag

    def search_customer_by_name(self, name):
        flag = False
        for r in range(1, self.get_no_of_rows()+1):
            table = self.driver.find_element(By.XPATH, self.tableXpath)
            customer_name = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[3]").text
            if customer_name == name:
                flag = True

        return flag





