import os
import pytest  # type: ignore[import]

from selenium import webdriver  # type: ignore[import]
from selenium.webdriver.chrome.service import Service  # type: ignore[import]
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore[import]


# Base URL Fixture
@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


# Driver Fixture
@pytest.fixture(scope="function")
def driver(request):

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    # Store driver in request for screenshot hook
    request.node.driver = driver

    yield driver

    driver.quit()


# Screenshot on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = getattr(item, "driver", None)

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}_failure.png"
            )

            driver.save_screenshot(screenshot_path)