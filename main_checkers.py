import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class regression(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.own_checks = (By.XPATH, '//*[@src="you1.gif"]')
        self.space_02 = (By.XPATH,'//*[@name="space02"]')
        self.space_13 = (By.XPATH, '//*[@name="space13"]')
        self.space_22 = (By.XPATH,'//*[@name="space22"]')
        self.space_33 = (By.XPATH, '//*[@name="space33"]')

    def test_get_ole(self):
        self.driver.get('https://www.gamesforthebrain.com/game/checkers/')
        time.sleep(5)
        amount_of_own_checks_start = len(self.driver.find_elements(*self.own_checks))
        self.driver.find_element(*self.space_02).click()
        time.sleep(2)
        self.driver.find_element(*self.space_13).click()
        time.sleep(2)
        self.driver.find_element(*self.space_22).click()
        time.sleep(2)
        self.driver.find_element(*self.space_33).click()
        amount_of_own_checks_after_2_moves = len(self.driver.find_elements(*self.own_checks))
        self.assertTrue(amount_of_own_checks_start > amount_of_own_checks_after_2_moves)
        print(amount_of_own_checks_start)
        print(amount_of_own_checks_after_2_moves)

