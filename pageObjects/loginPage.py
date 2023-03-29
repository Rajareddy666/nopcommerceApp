from selenium import webdriver
from selenium.webdriver.common.by import By

class login:
    text_username_id="Email"
    text_password_id="Password"
    click_login_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="Logout"
    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID,self.text_username_id).clear()
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)
    def setlogin(self):
        self.driver.find_element(By.XPATH,self.click_login_xpath).click()
    def setlogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
