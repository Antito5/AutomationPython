import unittest

from selenium.webdriver.common.by import By


class IndexPage(unittest.TestCase):

    LOGIN_BUTTON = (By.XPATH, '//*[@id="customer_menu_top"]/li/a')

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

