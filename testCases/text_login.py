import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import read_config
from utilites.customLogger import LoginGen

class Test001Login:
    baseUrl = read_config.getApplicationURL()
    username = read_config.getUserEmail()
    password = read_config.getUserPassword()
    logger = LoginGen.loggen()

    @pytest.mark.sanity

    def test_homepage_title(self, setup):
        self.logger.info("****************** Test001Login ****************")
        self.logger.info("********** verifying Homepage Title *********** ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** Homepage Title passed  *************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.error("******* Homepage Title Verification Failed return False ******")
            assert False

    def test_login(self, setup):
        self.logger.info("********* Verifying Test Login ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":

            assert True
            self.driver.close()
            self.logger.info("******* Test Login Passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
            self.logger.error("****** Login Test Verification Failed return False *******")
            self.driver.close()
            assert False
