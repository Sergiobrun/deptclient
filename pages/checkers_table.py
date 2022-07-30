from selenium.webdriver.common.by import By

class table():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.own_check = (By.XPATH, '//*[@src="you1.gif"]')

    def get_amount_own_checks(self):
        return self.driver.find_elements(*self.own_check).click()
