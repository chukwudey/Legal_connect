from selenium.webdriver.common.by import By


class ClientLoginPageLocators:
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN1 = (By.ID, "login_button")
    LOGIN = (By.XPATH, '/html/body/lc-root/app-site/div/mat-toolbar/div/div[2]/div[2]/a[1]')
    CLIENT = (By.XPATH,'//*[@id="mat-menu-panel-2"]/div/button[1]')