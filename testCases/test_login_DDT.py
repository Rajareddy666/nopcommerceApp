import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import login
from utilities import xlUtilis

class Test_login:
    baseurl = Readconfig.geturl()
    path= "C:\\Users\\hp\\PycharmProjects\\nopommerceApp\\TestData\\test_data.xlsx"
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_DDT_login(self,setup):
        self.logger.info("*** Verify Login DDT Test ***")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=login(self.driver)
        self.rows = xlUtilis.getRowCount(self.path,"Sheet1")
        print("no.of rows:",self.rows)
        list_status=[]
        for r in range(2,self.rows+1):
            self.user = xlUtilis.readData(self.path,"Sheet1",r,1)
            self.password = xlUtilis.readData(self.path, "Sheet1", r, 2)
            self.exp = xlUtilis.readData(self.path, "Sheet1", r, 3)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.setlogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("Passed")
                    self.lp.setlogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Fail")
                    self.lp.setlogout()
                    list_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("Fail")
                    self.lp.setlogout()
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("Passed")
                    self.lp.setlogout()
                    list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info("DDT TEST CASE Passed")
            self.driver.close()
            assert True

        else:
            self.logger.info("login DDT Test Case Fail")
            self.driver.close()
            assert False

