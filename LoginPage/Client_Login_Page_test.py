import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ClientLoginLocator.Client_Login_Locatotor_page import ClientLoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_login(self):
        click_login = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClientLoginPageLocators.LOGIN))
        click_login.click()

        time.sleep(3)

    def click_ima_client(self):
        click_im_client = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClientLoginPageLocators.CLIENT))
        click_im_client.click()

        time.sleep(3)

    def enter_email(self, username):
        enter_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClientLoginPageLocators.EMAIL))
        enter_email.send_keys(username)

        time.sleep(6)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClientLoginPageLocators.PASSWORD))
        enter_password.send_keys(password)

        time.sleep(3)

    def click_login1(self):
        click_login1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClientLoginPageLocators.LOGIN1))
        click_login1.click()

        time.sleep(6)
