

'''#import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.opencart.com/")
driver.find_element(By.LINK_TEXT, "LOGIN").click()

driver.find_element(By.NAME, "email").send_keys("mukulmangde3@gmail.com")

# enter lastname as wick
driver.find_element(By.NAME, "password").send_keys("123456789")

driver.find_element(By.CLASS_NAME, "btn-primary").click()

driver.find_element(By.ID, 'input-pin').send_keys("9881")

driver.find_element(By.XPATH, "//button[text()='Continue']").click()

expexted = driver.find_element(By.XPATH, "//a[contains(text(),'Details')]").text
print(expexted)'''


#project
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



driver = webdriver.Chrome()
detail = DetailsPage(driver)
while True:
    print("Enter 1 for LOGIN ")
    print("Enter 2 for VERIFY THE TEXT")
    print("Enter 3 for CHECKING XPATH")
    print("Enter 4 to Exit")
    userchoice = int(input())
    if userchoice == 1:
        detail.login("mukulmangde3@gmail.com", "123456789")
    elif userchoice == 2:
        print(detail.get_details_text())
    elif userchoice == 3:
        detail.exp()
    elif userchoice ==4:
            quit()
