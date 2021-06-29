import unittest

from selenium.webdriver.common.by import By


class LoginPage(unittest.TestCase):

    CONTINUE_BUTTON = (By.XPATH, '//*[@id="accountFrm"]/fieldset/button/i')

    def __init__(self, driver):
        self.driver = driver

    def go_to_register_page(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
