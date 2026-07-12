from selenium.webdriver.common.by import By  # type: ignore[import]
from pages.base_page import BasePage


class CheckboxPage(BasePage):

    SINGLE_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    def check_option(self, index=0):
        checkbox = self.wait_for_element(self.SINGLE_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self, index=0):
        checkbox = self.wait_for_element(self.SINGLE_CHECKBOX)
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self, index=0):
        checkbox = self.wait_for_element(self.SINGLE_CHECKBOX)
        return checkbox.is_selected()