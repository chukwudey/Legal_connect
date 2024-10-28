import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from LoginPage.Select_Client_Login_Page_test import LoginPage


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
    login_page.login_url("https://staging.legalconnectonline.com/legalconnect-identityserver/Account/Login?ReturnUrl=%2Flegalconnect-identityserver%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DlegalConnect_clients_web_client%26redirect_uri%3Dhttps%253A%252F%252Fstaging.legalconnectonline.com%252Flegalconnect-portal-client%252Fclient%26response_type%3Dcode%26scope%3Dprofile%2520openid%2520offline_access%2520legalConnect_identity_server_api%2520legalConnect_notification_api%2520legalConnect_appointment_api%2520legalConnect_client_api%2520legalConnect_clients_api_gateway%2520client_permissions%2520legalConnect_payment_api%2520legalConnect_lawyer_api%2520legalConnect_document_api%26nonce%3D2dfeb6a36fc46c0e1db294a85e61c42d6eRc3bHkY%26state%3Dab26258dcdbdfecf62afa587751fd58906ZJYOVNT%26code_challenge%3DUsTpJfiL9-W3eT9RIMD5JjxX5Ae4Btt3fDOaW1NqTj8%26code_challenge_method%3DS256")
    return login_page


def test_client_Login_test(login):
    login.click_login()
    login.click_ima_client()
    login.enter_email("chuks.julian.cj@gmail.com")
    login.enter_password("Imokom34@")
    login.click_login1()
