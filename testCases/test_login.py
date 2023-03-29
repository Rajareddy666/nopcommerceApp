import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import login

class Test_login:
    baseurl = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_homepage(self,setup):
        self.logger.info("*** Verify Login Test ***")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            self.logger.info("*** Title is passed ***")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\hp\\PycharmProjects\\nopommerceApp\\Screenshots\\"+"test_homepage.png")
            self.driver.close()
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*** Verify Login Test 2 ***")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.setlogin()
        self.lp.setlogout()
        time.sleep(5)





