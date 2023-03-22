import time

from utilites.customLogger import LoginGen
from utilites.readProperties import read_config
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustPage import AddCustomer


class Test004SearchbyName:
    baseUrl = read_config.getApplicationURL()
    username = read_config.getUserEmail()
    password = read_config.getUserPassword()
    logger = LoginGen.loggen()

    def testsearchbycust(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.driver.maximize_window()
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        time.sleep(3)
        self.addcust.clickoncustomersmenuitem()
        self.sc = SearchCustomer(self.driver)
        self.sc.setFname("Victoria")
        time.sleep(2)
        self.sc.setLname("Terces")
        self.sc.clickonSearch()
        time.sleep(2)
        search = self.sc.searchbyname("Victoria Terces")
        assert True == search
        self.logger("*********** test passed 004 *******")
        self.driver.close()

