from selenium.webdriver.common.by import By
class SearchCustomer:
    txt_email_id ="SearchEmail"
    txt_first_name_id="SearchFirstName"
    txt_lastname_id="SearchLastName"
    btn_search_id="search-customers"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_column_xpath="//table[@id='customers-grid']//tbody/tr/td"
    def __init__(self,driver):
        self.driver=driver
    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).clear()
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)

    def setfirstname(self,fstname):
        self.driver.find_element(By.ID,self.txt_first_name_id).clear()
        self.driver.find_element(By.ID,self.txt_first_name_id).send_keys(fstname)
    def setlastname(self,lstname):
        self.driver.find_element(By.ID,self.txt_lastname_id).clear()
        self.driver.find_element(By.ID,self.txt_lastname_id).send_keys(lstname)
    def setsearch(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()
    def getnoofrows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))
    def getnoofColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_column_xpath))
    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getnoofrows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();",table)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+(str(r))+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag
