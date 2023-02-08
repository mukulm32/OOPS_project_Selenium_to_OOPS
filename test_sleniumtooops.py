#import sleniumtooops as sl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginOpenCart:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def login(self, email, password):
        self.driver.get("https://www.opencart.com/")
        self.driver.find_element(By.LINK_TEXT, "LOGIN").click()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        self.driver.find_element(By.ID, 'input-pin').send_keys("9881")
        self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()

class DetailsPage(LoginOpenCart):
    def get_details_text(self):
        expected = self.driver.find_element(By.XPATH, "//a[contains(text(),'Details')]").text
        return expected

    def exp(self):
        try:
            self.driver.find_element(By.LINK_TEXT,"LOGIN").click()
            print("processing ")
        except:
            print("error! check for xpath")


@pytest.fixture(scope='class')
def setup_driver():
    driver = webdriver.Chrome()
    detail = DetailsPage(driver)
    yield detail
    driver.quit()

class TestLoginOpenCart:
    def test_login(self, setup_driver):
        setup_driver.login("mukulmangde3@gmail.com", "123456789")
        actual_text = setup_driver.get_details_text()
        assert actual_text == 'Account Details', f"Expected text is 'Account Details' but got '{actual_text}'"

    def test_xpath_check(self, setup_driver):
        setup_driver.exp()
        assert setup_driver.driver.find_element(By.LINK_TEXT, "LOGIN").text == "LOGIN", "Could not find LOGIN link"