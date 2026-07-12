import pytest  # type: ignore[import]
from selenium import webdriver  # type: ignore[import]
from selenium.webdriver.chrome.service import Service  # type: ignore[import]
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore[import]


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"