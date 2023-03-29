import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import login
from pageObjects.AddCustomer import AddCustomer
class Test_Customer:
    baseurl = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_AddCustomer(self,setup):
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
        self.addcut.AddNew()

        self.logger.info("** providing customer info **")
        self.email = random_gnerator() + "@gmail.com"
        self.addcut.SetEmail(self.email)
        self.addcut.SetPassword("124")
        self.addcut.SetFirstName("Raja Reddy")
        self.addcut.SetLastName("Gangikunta")
        self.addcut.Setrd_gender("Male")
        self.addcut.Setdob("4/15/1999")
        self.addcut.SetcompanyName("QA-Roadmap")
        self.addcut.SetNewsLetter("Test store 2")
        self.addcut.Setmanager_vendor("Vendor 1")
        self.addcut.SetAdmincontext("This is Testing......")
        self.addcut.Setsave_details()

        self.logger.info("*** saving customer info ***")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("Add Customer Test Passed")
        else:
            self.driver.save_screenshot("C:\\Users\\hp\\PycharmProjects\\nopommerceApp\\Screenshots\\" + "test_homepage.png")
            self.logger.error("Add Customer Test Failed")
            assert False
        self.driver.close()


def random_gnerator(size=8,chars=string.ascii_lowercase + string.digits ):
    return "".join(random.choice(chars)for x in range(size))