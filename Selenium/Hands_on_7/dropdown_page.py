from selenium.webdriver.support.ui import Select  # type: ignore[import]

from pages.base_page import BasePage


class DropdownPage(BasePage):

    DAY_DROPDOWN = ("id", "select-demo")

    def select_day(self, day_name):
        dropdown = Select(
            self.wait_for_element(self.DAY_DROPDOWN)
        )
        dropdown.select_by_visible_text(day_name)