import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    lnk_customer_xpath="(//a[@class='nav-link'])[21]"
    lnk_customer_drp_xpath= "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_xpath = "//a[normalize-space()='Add new']"
    email_id = "Email"
    Password_id = "Password"
    Firstname_id= "FirstName"
    Lastname_id = "LastName"
    rd_btn_male_id ="Gender_Male"
    rd_btn_female_id = "Gender_Female"
    DOB_id="DateOfBirth"
    company_name_id="Company"
    news_xpath_store="(//li[@role='option'])[1]"
    news_xpath_name = "//*[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/li[2]"

    manager_of_vendor_xpath= "//select[@id='VendorId']"
    bth_Active_id="Active"
    Admin_comment_id = "AdminComment"
    btn_save_xpath="//button[@name='save']"
    def __init__(self,driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_customer_xpath).click()
    def clickonCustomerMenuitem(self):
        self.driver.find_element(By.XPATH,self.lnk_customer_drp_xpath).click()
    def AddNew(self):
        self.driver.find_element(By.XPATH,self.btn_add_new_xpath).click()
    def SetEmail(self,email):
        self.driver.find_element(By.ID,self.email_id).send_keys(email)
    def SetPassword(self,password):
        self.driver.find_element(By.ID,self.Password_id).send_keys(password)
    def SetFirstName(self, firstname):
        self.driver.find_element(By.ID, self.Firstname_id).send_keys(firstname)
    def SetLastName(self, lastname):
        self.driver.find_element(By.ID, self.Lastname_id).send_keys(lastname)
    def Setrd_gender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID,self.rd_btn_male_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID,self.rd_btn_female_id).click()
    def Setdob(self,DOB):
        self.driver.find_element(By.ID,self.DOB_id).send_keys(DOB)
    def SetcompanyName(self,compName):
        self.driver.find_element(By.ID,self.company_name_id).send_keys(compName)
    def SetNewsLetter(self,letter):
        self.driver.find_element(By.XPATH,"(//div[@class='k-widget k-multiselect k-multiselect-clearable'])[1]").click()
        if letter=="Test store 2":
            self.nl = self.driver.find_element(By.XPATH,self.news_xpath_store).click()


    def Setmanager_vendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.manager_of_vendor_xpath))
        drp.select_by_visible_text(value)
    def SetAdmincontext(self,content):
        self.driver.find_element(By.ID,self.Admin_comment_id).send_keys(content)
    def Setsave_details(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()




