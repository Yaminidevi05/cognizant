from selenium.webdriver.common.by import By  # type: ignore[import]
from pages.base_page import BasePage


class InputFormPage(BasePage):

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "inputEmail4")
    PASSWORD = (By.ID, "inputPassword4")
    COMPANY = (By.ID, "company")
    WEBSITE = (By.ID, "websitename")
    PHONE = (By.ID, "inputCity")
    ADDRESS = (By.ID, "inputAddress1")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_form(self, name, email, phone, address):

        self.wait_for_element(self.NAME).send_keys(name)
        self.wait_for_element(self.EMAIL).send_keys(email)

        # Required fields on the page
        self.wait_for_element(self.PASSWORD).send_keys("Password123")
        self.wait_for_element(self.COMPANY).send_keys("Cognizant")
        self.wait_for_element(self.WEBSITE).send_keys("www.test.com")

        self.wait_for_element(self.PHONE).send_keys(phone)
        self.wait_for_element(self.ADDRESS).send_keys(address)

    def submit_form(self):
        self.wait_for_element(self.SUBMIT).click()

    def get_page_title(self):
        return self.driver.title