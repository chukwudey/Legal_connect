import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from LoginPage.Client_Login_Page_test import LoginPage


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://staging.legalconnectonline.com/legalconnect-website-angular/")
    return login_page


def test_client_Login_test(login):
    login.click_login()
    login.click_ima_client()
    login.enter_email("chuks.julian.cj@gmail.com")
    login.enter_password("Imokom34@")
    login.click_login1()
