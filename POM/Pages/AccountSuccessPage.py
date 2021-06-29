import unittest
from selenium.webdriver.common.by import By


class AccountSuccessPage(unittest.TestCase):
    OK_MESSAGE = (By.XPATH, '//*[@id="maincontainer"]/div/div[1]/div/h1/span[1]')
    OK_SUBTITLE = (By.XPATH, '//*[@id="maincontainer"]/div/div[1]/div/div/section/p[2]')

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*self.OK_MESSAGE).text

    def get_subtitle(self):
        return self.driver.find_element(*self.OK_SUBTITLE).text
