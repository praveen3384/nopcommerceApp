from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = (By.ID, 'Email')
    textbox_password_id = (By.ID, 'Password')
    button_login_xpath = (By.XPATH, "//button[@type='submit']")
    link_logout_xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(*self.textbox_username_id).clear()
        self.driver.find_element(*self.textbox_username_id).send_keys(username)


    def set_password(self, password):
        self.driver.find_element(*self.textbox_password_id).clear()
        self.driver.find_element(*self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(*self.link_logout_xpath).click()

