from selenium.webdriver.support.wait import WebDriverWait  # type: ignore[reportMissingImports]
from selenium.webdriver.support import expected_conditions as EC  # type: ignore[reportMissingImports]


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )