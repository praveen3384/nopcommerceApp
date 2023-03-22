import random
import string
import time

from selenium.webdriver.common.by import By

from pageObjects.AddCustPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import read_config
from utilites.customLogger import LoginGen

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return '' .join(random.choice(chars) for x in range(size))

class Test003_AddCustomer:
    baseUrl = read_config.getApplicationURL()
    username = read_config.getUserEmail()
    password = read_config.getUserPassword()
    logger = LoginGen.loggen()

    def testaddcustomer(self, setup):
        self.logger.info("****************** Test003 Add Customer  ****************")
        self.logger.info("********** verifying Add Customer *********** ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.driver.maximize_window()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        time.sleep(1)
        self.addcust.clickoncustomersmenuitem()
        self.addcust.clickonaddnew()
        self.email = random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("pass123")
        self.addcust.setfirstname("Praveen")
        self.addcust.setgender("Male")
        self.addcust.setlastname("Kumar")
        self.addcust.setdob("01/01/2001")
        self.addcust.setcompanyname("cricket")
        self.addcust.clickontaxexempt()
        # self.addcust.setcustomersrole("ForumModerators")
        self.addcust.setmanagerofvendor("Vendor 2")
        # self.addcust.setnewsletter("abbbibbi")
        self.addcust.clickonsave()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\addcustomer.png")
            assert True == False

        self.driver.close()



