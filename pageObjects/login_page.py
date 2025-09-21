''' login page class'''
from selenium.webdriver.common.by import By


class LoginPage:
    '''
    locators are assigned
    to the variables
    '''
    textbox_username_id = "//input[@id='Email']"
    textbox_password_id = "//input[@id='Password']"
    login_button = "//button[@type='submit']"
    logout_link_txt = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        ''' setting username to enter'''
        self.driver.find_element(By.XPATH,
                                 self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH,
                                 self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        '''setting password to enter in password field'''
        self.driver.find_element(By.XPATH,
                                 self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH,
                                 self.textbox_password_id).send_keys(password)

    def click_login_button(self):
        '''this function applies login method'''
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_logout_button(self):
        '''this function applies logout '''
        self.driver.find_element(By.LINK_TEXT, self.logout_link_txt).click()
