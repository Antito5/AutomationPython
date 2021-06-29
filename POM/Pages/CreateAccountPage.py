import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateAccountPage(unittest.TestCase):
    FIRST_NAME_TXT = (By.XPATH, '//*[@id="AccountFrm_firstname"]')
    LAST_NAME_TXT = (By.XPATH, '//*[@id="AccountFrm_lastname"]')
    EMAIL_TXT = (By.XPATH, '//*[@id="AccountFrm_email"]')
    PHONE_TXT = (By.XPATH, '//*[@id="AccountFrm_telephone"]')
    FAX_TXT = (By.XPATH, '//*[@id="AccountFrm_fax"]')

    ##COMPANY
    COMPANY_TXT = (By.XPATH, '//*[@id="AccountFrm_company"]')
    COMPANY_ADDRESS1_TXT = (By.XPATH, '//*[@id="AccountFrm_address_1"]')
    COMPANY_ADDRESS2_TXT = (By.XPATH, '//*[@id="AccountFrm_address_2"]')
    CITY_TXT = (By.XPATH, '//*[@id="AccountFrm_city"]')
    REGION_LIST = (By.XPATH, '//*[@id="AccountFrm_zone_id"]')
    ZIP_CODE_TXT = (By.XPATH, '//*[@id="AccountFrm_postcode"]')
    COUNTRY_LIST = (By.XPATH, '//*[@id="AccountFrm_country_id"]')

    ##Login details
    LOGIN_NAME_TXT = (By.XPATH, '//*[@id="AccountFrm_loginname"]')
    PASSWORD_TXT = (By.XPATH, '//*[@id="AccountFrm_password"]')
    PASSWORD_CONFIRM_TXT = (By.XPATH, '//*[@id="AccountFrm_confirm"]')
    SUBSCRIBE_RADIO = (By.XPATH, '//*[@id="AccountFrm_newsletter0"]')

    AGREE_CHECK = (By.XPATH, '//*[@id="AccountFrm_agree"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="AccountFrm"]/div[5]/div/div/button')

    ##ERROR MESSAGES
    ##Required fields
    FIRST_NAME_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[1]/fieldset/div[1]/span')
    LASTNAME_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[1]/fieldset/div[2]/span')
    EMAIL_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[1]/fieldset/div[3]/span')
    ADDRESS1_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[2]/fieldset/div[2]/span')
    CITY_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[2]/fieldset/div[4]/span')
    REGION_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[2]/fieldset/div[5]/span')
    ZIP_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[2]/fieldset/div[6]/span')
    USERNAME_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[3]/fieldset/div[1]/span')
    PASSWORD_ERROR_REQUIRED = (By.XPATH, '//*[@id="AccountFrm"]/div[3]/fieldset/div[2]/span')

    AGREE_ERROR = (By.XPATH, '//*[@id="maincontainer"]/div/div/div/div[1]')

    def __init__(self, driver):
        self.driver = driver

    def complete_register(self, name, lastname, email, phone, fax, company, address1, address2, city, region, zip,
                          country, login_name, password, password2):
        self.driver.find_element(*self.FIRST_NAME_TXT).send_keys(name)
        self.driver.find_element(*self.LAST_NAME_TXT).send_keys(lastname)
        self.driver.find_element(*self.EMAIL_TXT).send_keys(email)
        self.driver.find_element(*self.PHONE_TXT).send_keys(phone)
        self.driver.find_element(*self.FAX_TXT).send_keys(fax)
        self.driver.find_element(*self.COMPANY_TXT).send_keys(company)
        self.driver.find_element(*self.COMPANY_ADDRESS1_TXT).send_keys(address1)
        self.driver.find_element(*self.COMPANY_ADDRESS2_TXT).send_keys(address2)
        self.driver.find_element(*self.CITY_TXT).send_keys(city)
        Select(self.driver.find_element(*self.COUNTRY_LIST)).select_by_visible_text(country)
        self.driver.find_element(*self.ZIP_CODE_TXT).send_keys(zip)
        self.driver.find_element(*self.LOGIN_NAME_TXT).send_keys(login_name)
        self.driver.find_element(*self.PASSWORD_TXT).send_keys(password)
        self.driver.find_element(*self.PASSWORD_CONFIRM_TXT).send_keys(password2)
        Select(self.driver.find_element(*self.REGION_LIST)).select_by_visible_text(region)
        self.driver.find_element(*self.SUBSCRIBE_RADIO).click()
        self.driver.find_element(*self.AGREE_CHECK).click()
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def completeRegister_without_requiredFields(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def getErrorMessage_requiredName(self):
        return self.driver.find_element(*self.FIRST_NAME_ERROR_REQUIRED).text

    def getErrorMessage_requiredLastname(self):
        return self.driver.find_element(*self.LASTNAME_ERROR_REQUIRED).text

    def getErrorMessage_requiredEmail(self):
        return self.driver.find_element(*self.EMAIL_ERROR_REQUIRED).text

    def getErrorMessage_requiredAddress1(self):
        return self.driver.find_element(*self.ADDRESS1_ERROR_REQUIRED).text

    def getErrorMessage_requiredCity(self):
        return self.driver.find_element(*self.CITY_ERROR_REQUIRED).text

    def getErrorMessage_requiredRegion(self):
        return self.driver.find_element(*self.REGION_ERROR_REQUIRED).text

    def getErrorMessage_requiredZip(self):
        return self.driver.find_element(*self.ZIP_ERROR_REQUIRED).text

    def getErrorMessage_requiredUsername(self):
        return self.driver.find_element(*self.USERNAME_ERROR_REQUIRED).text

    def getErrorMessage_requiredPassword(self):
        return self.driver.find_element(*self.PASSWORD_ERROR_REQUIRED).text

    def getErrorMessage_requiredAgreeCheck(self):
        return self.driver.find_element(*self.AGREE_ERROR).text
