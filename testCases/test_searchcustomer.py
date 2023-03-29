import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import login
from pageObjects.searchCustomer import SearchCustomer
from pageObjects.AddCustomer import AddCustomer
class Test_Customer:
    baseurl = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_searchCustomer(self,setup):
        self.logger.info("*** login to webpage ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.setlogin()
        self.logger.info("** Successfully Login ***")

        self.addcut = AddCustomer(self.driver)
        self.addcut.clickonCustomerMenu()
        self.addcut.clickonCustomerMenuitem()

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.setsearch()
        time.sleep(4)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.driver.close()
