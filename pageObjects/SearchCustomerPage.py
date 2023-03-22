from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_email_id = (By.ID, "SearchEmail")
    txt_firstname_id = (By.ID, "SearchFirstName")
    txt_lastname_id = (By.ID, "SearchLastName")
    btn_search_xpath = (By.XPATH, "//button[@id='search-customers']")
    table_searchresults_xpath = (By.XPATH, "//div[@class='dataTables_scrollHead']")
    table_xpath = (By.XPATH, "//table[@id='customers-grid']")
    table_rows_xpath = (By.XPATH, "//table[@id='customers-grid']//tbody/tr")
    table_columns_xpath = (By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, Email):
        self.driver.find_element(*self.txt_email_id).clear()
        self.driver.find_element(*self.txt_email_id).send_keys(Email)

    def setFname(self, Fname):
        self.driver.find_element(*self.txt_firstname_id).clear()
        self.driver.find_element(*self.txt_firstname_id).send_keys(Fname)

    def setLname(self, Lname):
        self.driver.find_element(*self.txt_lastname_id).clear()
        self.driver.find_element(*self.txt_lastname_id).send_keys(Lname)

    def clickonSearch(self):
        self.driver.find_element(*self.btn_search_xpath).click()

    def getNoofRows(self):
        return len(self.driver.find_elements_by_xpath(self.table_rows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements_by_xpath(self.table_columns_xpath))

    def searchbyemail(self, email):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
            return flag

    def searchbyname(self, Name1):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]")
            if name == Name1:
                flag = True
                break
            return flag




