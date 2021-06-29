import time
import unittest

from selenium import webdriver

from POM.Pages.AccountSuccessPage import AccountSuccessPage
from POM.Pages.CreateAccountPage import CreateAccountPage
from POM.Pages.IndexPage import IndexPage
from POM.Pages.LoginPage import LoginPage


class CreateAccountTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\Admin\\PycharmProjects\\AutomationStore\\Drivers\\chromedriver.exe")
        self.driver.get("https://automationteststore.com/")

    def test_register_newUser_OK(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)
        create_account_page = CreateAccountPage(self.driver)
        account_success = AccountSuccessPage(self.driver)

        ##Paso 1: Seleccionar botón "Login or register"
        index_page.go_to_login_page()

        ##Paso 2: seleccionar boton continue
        login_page.go_to_register_page()

        ##Paso 3- completar todos los campos
        create_account_page.complete_register('Morano', 'Antonella', 'antoooo@hotmail.com', '3524345677',
                                              '3527484033', 'DARWOFT', 'capitalinas 123', 'lalalal 123', 'Cordoba',
                                              'Cordoba', '5000', 'Argentina', 'antito2906', '12345678910',
                                              '12345678910')

        # Validar que la cuenta se creó correctamente
        time.sleep(5)
        print(account_success.get_title())
        print(account_success.get_subtitle())
        assert account_success.get_title() == 'YOUR ACCOUNT HAS BEEN CREATED!'
        assert account_success.get_subtitle() == 'Congratulations! Your new account has been successfully created!'

    def test_register_newUser_NoOk_requiredFields(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)
        create_account_page = CreateAccountPage(self.driver)

        ##Paso 1: Seleccionar botón "Login or register"
        index_page.go_to_login_page()

        ##Paso 2: seleccionar boton continue
        login_page.go_to_register_page()

        ##Paso 3- completar todos los campos
        create_account_page.completeRegister_without_requiredFields()

        # Validar que la cuenta se creó correctamente
        time.sleep(5)

        assert create_account_page.getErrorMessage_requiredName() == 'First Name must be between 1 and 32 characters!'
        assert create_account_page.getErrorMessage_requiredLastname() == 'Last Name must be between 1 and 32 characters!'
        assert create_account_page.getErrorMessage_requiredEmail() == 'Email Address does not appear to be valid!'
        assert create_account_page.getErrorMessage_requiredAddress1() == 'Address 1 must be between 3 and 128 characters!'
        assert create_account_page.getErrorMessage_requiredCity() == 'City must be between 3 and 128 characters!'
        assert create_account_page.getErrorMessage_requiredRegion() == 'Please select a region / state!'
        assert create_account_page.getErrorMessage_requiredZip() == 'Zip/postal code must be between 3 and 10 characters!'
        assert create_account_page.getErrorMessage_requiredUsername() == 'Login name must be alphanumeric only and between 5 and 64 characters!'
        assert create_account_page.getErrorMessage_requiredPassword() == 'Password must be between 4 and 20 characters!'
        assert create_account_page.getErrorMessage_requiredAgreeCheck() == '×\nError: You must agree to the Privacy Policy!'
