import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    link_customersmenu_xpath = (By.XPATH, "(//p[contains(text(),'Customers')])[1]")
    link_customersmenuitem_xpath = (By.XPATH, "(//p[contains(text(),'Customers')])[2]")
    btn_addnew_xpath = (By.XPATH, "//a[normalize-space()='Add new']")
    txt_email_id = (By.ID, "Email")
    txt_password_id = (By.ID, "Password")
    txt_firstname_id = (By.ID, "FirstName")
    txt_lastname_id = (By.ID, "LastName")
    rb_male_id = (By.ID, "Gender_Male")
    rb_female_id = (By.ID, "Gender_Female")
    txt_dob_id = (By.ID, "DateOfBirth")
    txt_companyname_id = (By.ID, "Company")
    rb_istaxexempt_id = (By.ID, "IsTaxExempt")
    txt_newsletter_xpath = (By.XPATH, "//div[@class='input-group-append']//div[@role='listbox']")
    txt_customerroles_xpath = (By.XPATH, "(//div[@role='listbox'])[2]")
    lstitem_adminstrators_xpath = (By.XPATH, "//li[contains(text(),'Administrators')]")
    lstitem_ForumModerators_xpath = (By.XPATH, "//li[contains(text(),'Forum Moderators')]")
    lstitem_Guests_xpath = (By.XPATH, "//li[contains(text(),'Guests')]")
    lstitem_Registered_xpath = (By.XPATH, "//li[contains(text(),'Registered')]")
    lstitem_Vendors_xpath = (By.XPATH, "//li[contains(text(),'Vendors')]")
    lst_managerofvendor_xpath = (By.XPATH, "//select[@id='VendorId']")
    txt_admincomment_xpath = (By.XPATH, "//textarea[@id='AdminComment']")
    btn_save_xpath = (By.XPATH, "(//button[@name='save'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def clickoncustomersmenu(self):
        self.driver.find_element(*self.link_customersmenu_xpath).click()

    def clickoncustomersmenuitem(self):
        self.driver.find_element(*self.link_customersmenuitem_xpath).click()

    def clickonaddnew(self):
        self.driver.find_element(*self.btn_addnew_xpath).click()

    def setemail(self, email):
        self.driver.find_element(*self.txt_email_id).clear()
        self.driver.find_element(*self.txt_email_id).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(*self.txt_password_id).clear()
        self.driver.find_element(*self.txt_password_id).send_keys(password)

    def setfirstname(self, firstname):
        self.driver.find_element(*self.txt_firstname_id).clear()
        self.driver.find_element(*self.txt_firstname_id).send_keys(firstname)

    def setlastname(self, lastname):
        self.driver.find_element(*self.txt_lastname_id).clear()
        self.driver.find_element(*self.txt_lastname_id).send_keys(lastname)

    def setdob(self, dob):
        self.driver.find_element(*self.txt_dob_id).clear()
        self.driver.find_element(*self.txt_dob_id).send_keys(dob)

    def setcompanyname(self, comname):
        self.driver.find_element(*self.txt_companyname_id).clear()
        self.driver.find_element(*self.txt_companyname_id).send_keys(comname)

    def clickontaxexempt(self):
        self.driver.find_element(*self.txt_companyname_id).clear()

    def setmanagerofvendor(self, value):
        drpvendor = Select(self.driver.find_element(*self.lst_managerofvendor_xpath))
        drpvendor.select_by_visible_text(value)

    def setnewsletter(self, newsletter):
        self.driver.find_element(*self.txt_newsletter_xpath).clear()
        self.driver.find_element(*self.txt_newsletter_xpath).send_keys(newsletter)

    def setgender(self, gender):
        if gender == "Male":
            self.driver.find_element(*self.rb_male_id).click()
        elif gender == "Female":
            self.driver.find_element(*self.rb_female_id).click()
        else:
            self.driver.find_element(*self.rb_male_id).click()

    def setcustomersrole(self, role):
        self.driver.find_element(*self.txt_customerroles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(*self.lstitem_Registered_xpath).click()
        elif role == "Administrators":
            self.listitem = self.driver.find_element(*self.lstitem_adminstrators_xpath).click()
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]")
            self.listitem = self.driver.find_element(*self.lstitem_Guests_xpath).click()

        elif role == "ForumModerators":
            self.listitem = self.driver.find_element(*self.lstitem_ForumModerators_xpath).click()

        elif role == "Vendors":
            self.listitem = self.driver.find_element(*self.lstitem_Vendors_xpath).click()

        else:
            self.listitem = self.driver.find_element(*self.lstitem_Guests_xpath).click()

        time.sleep(3)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def clickonsave(self):
        self.driver.find_element(*self.btn_save_xpath).click()
