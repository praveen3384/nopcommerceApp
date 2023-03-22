import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import read_config
from utilites.customLogger import LoginGen
from utilites import XLUtilis


class Test_002_DDT_Login:
    baseUrl = read_config.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LoginGen.loggen()

    @pytest.mark.regression

    def test_login(self, setup):
        self.logger.info("****************** Test002_DDT_Login ****************")
        self.logger.info("********* Verifying Test Login ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.rows = XLUtilis.getRowCount(self.path, 'Sheet1')
        list_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtilis.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtilis.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtilis.readData(self.path, 'Sheet1', r, 3)
            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("***** Test Pass *****")
                    self.lp.click_logout()
                    time.sleep(5)
                    list_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("****** Test failed *******")
                    self.lp.click_logout()
                    list_status.append("fail")
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("***** Test failed  *****")
                    list_status.append("fail")
                elif self.exp == 'fail':
                    self.logger.info("****** Test passed *****")
                    list_status.append("pass")
                    print(list_status)
        if "fail" not in list_status:
            self.logger.info("***** Login Test ddt passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.error("******** Login Test ddt failed ******")
            self.driver.close()
            assert False

        self.logger.info("****************** Verified Test_002_DDT_Login ****************")
        self.logger.info("****************  Completed Test_002_DDT_Login  ***************")
