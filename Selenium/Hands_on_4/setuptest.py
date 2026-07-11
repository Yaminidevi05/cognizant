"""
===========================================================
HANDS-ON 4 - Selenium WebDriver Setup & Basic Commands
===========================================================

Selenium Components:

1. WebDriver
   - WebDriver is the core component of Selenium used to automate browsers.
   - It communicates directly with the browser through the browser driver
     (such as ChromeDriver) using the WebDriver protocol.
   - It performs actions like opening pages, clicking buttons,
     entering text, and retrieving page information.

2. Selenium Grid
   - Selenium Grid allows tests to run on multiple machines,
     browsers, and operating systems simultaneously.
   - It solves the problem of slow execution by enabling
     parallel testing across different environments.

3. Selenium IDE
   - Selenium IDE is a browser extension.
   - It is mainly used for recording and playing back user actions.
   - It can also generate automation code in multiple programming languages.
"""

from selenium import webdriver  # type: ignore[import]
from selenium.webdriver.common.by import By  # type: ignore[import]
from selenium.webdriver.chrome.service import Service  # type: ignore[import]
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore[import]

# -------------------------------------------------------
# Chrome Options
# -------------------------------------------------------
options = webdriver.ChromeOptions()

# Run browser in headless mode
options.add_argument("--headless=new")

# Optional window size for headless mode
options.add_argument("--window-size=1280,800")

# Create driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# -------------------------------------------------------
# Implicit Wait
# -------------------------------------------------------
driver.implicitly_wait(10)

# Why implicit wait is not recommended?
#
# Implicit wait applies globally to every element search.
# It may unnecessarily slow down tests and can conflict with
# Explicit Waits. Explicit waits are preferred because they
# wait only for specific conditions and make tests faster
# and more reliable.

# -------------------------------------------------------
# Task 1
# -------------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:")
print(driver.title)

# -------------------------------------------------------
# Task 2
# -------------------------------------------------------

# Click Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("\nCurrent URL:")
print(driver.current_url)

# Go Back
driver.back()

print("\nReturned to:")
print(driver.title)

# -------------------------------------------------------
# Open New Tab
# -------------------------------------------------------

driver.execute_script('window.open("https://www.google.com");')

print("\nWindow Handles:")
print(driver.window_handles)

# Switch to Google Tab
driver.switch_to.window(driver.window_handles[1])

print("\nGoogle Tab Title:")
print(driver.title)

# -------------------------------------------------------
# Switch Back
# -------------------------------------------------------

driver.switch_to.window(driver.window_handles[0])

# Screenshot
driver.save_screenshot("playground_screenshot.png")

print("\nScreenshot saved as playground_screenshot.png")

# -------------------------------------------------------
# Window Size
# -------------------------------------------------------

print("\nCurrent Window Size:")
print(driver.get_window_size())

driver.set_window_size(1280, 800)

print("\nUpdated Window Size:")
print(driver.get_window_size())

# Why use a fixed window size?
#
# A consistent browser size ensures responsive UI behaves
# predictably. Different window sizes can change page layouts,
# causing element locations and test results to vary.

# -------------------------------------------------------
# Close Browser
# -------------------------------------------------------

driver.quit()

print("\nBrowser Closed Successfully.")