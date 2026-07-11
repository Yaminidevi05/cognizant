from selenium import webdriver  # type: ignore[import]
from selenium.webdriver.common.by import By  # type: ignore[import]
from selenium.webdriver.chrome.service import Service  # type: ignore[import]
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore[import]
from selenium.webdriver.support import expected_conditions as EC  # type: ignore[import]
from selenium.common.exceptions import NoSuchElementException  # type: ignore[import]

try:
    # import via importlib to avoid static analysis false-positives in some editors
    import importlib
    ChromeDriverManager = importlib.import_module("webdriver_manager.chrome").ChromeDriverManager
except Exception:
    print("Warning: webdriver_manager not installed. Install with: pip install webdriver-manager")
    ChromeDriverManager = None

import time

# -------------------------------
# Browser Setup
# -------------------------------
# Use the imported Service class to create the Chrome service
if ChromeDriverManager:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
else:
    driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# ==========================================================
# TASK 1
# ==========================================================

driver.get("https://testmu.ai/selenium-playground/simple-form-demo/")

# Accept cookies if displayed
try:
    cookie = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        )
    )
    cookie.click()
except:
    pass

print("\n========== LOCATOR STRATEGIES ==========\n")

# Wait until input box appears
wait.until(
    EC.presence_of_element_located((By.ID, "user-message"))
)

# ---------------- ID ----------------
try:
    driver.find_element(By.ID, "user-message")
    print("ID Locator Working")
except:
    print("ID Locator Failed")

# ---------------- NAME ----------------
try:
    driver.find_element(By.NAME, "message")
    print("NAME Locator Working")
except:
    print("NAME Locator Failed")

# ---------------- CLASS ----------------
try:
    driver.find_element(By.CLASS_NAME, "form-control")
    print("CLASS_NAME Locator Working")
except:
    print("CLASS_NAME Locator Failed")

# ---------------- TAG ----------------
try:
    driver.find_element(By.TAG_NAME, "input")
    print("TAG_NAME Locator Working")
except:
    print("TAG_NAME Locator Failed")

# ---------------- XPATH ----------------
try:
    driver.find_element(By.XPATH, "//input[@id='user-message']")
    print("XPath Locator Working")
except:
    print("XPath Locator Failed")

# ---------------- CSS ----------------
try:
    driver.find_element(By.CSS_SELECTOR, "#user-message")
    print("CSS Locator Working")
except:
    print("CSS Locator Failed")

# ==========================================================
# CSS SELECTORS
# ==========================================================

print("\n========== CSS SELECTORS ==========\n")

try:
    driver.find_element(By.CSS_SELECTOR, "#user-message")
    print("CSS by ID Working")
except:
    print("CSS by ID Failed")

try:
    driver.find_element(By.CSS_SELECTOR, "input[name='message']")
    print("CSS by Attribute Working")
except:
    print("CSS by Attribute Failed")

try:
    driver.find_element(By.CSS_SELECTOR, "div.col-md-6 input")
    print("CSS Parent Child Working")
except:
    print("CSS Parent Child Failed")

# ==========================================================
# CHECKBOX DEMO
# ==========================================================

driver.get("https://testmu.ai/selenium-playground/checkbox-demo/")

wait.until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

print("\n========== CHECKBOX DEMO ==========\n")

try:
    label = driver.find_element(By.XPATH, "//*[contains(text(),'Option 1')]")
    print("Label:", label.text)
except:
    print("Option 1 Label Not Found")

labels = driver.find_elements(By.XPATH, "//*[contains(text(),'Option')]")

print("\nLabels found:")
for item in labels:
    print(item.text)

# ==========================================================
# TASK 2
# ==========================================================

driver.get("https://testmu.ai/selenium-playground/bootstrap-alert-messages-demo/")

# Wait until page loads
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Accept cookies if shown
try:
    cookie = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable(
            (By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        )
    )
    cookie.click()
except:
    pass

print("\n========== EXPLICIT WAIT ==========\n")

start = time.time()

button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,"//button[contains(text(),'Autocloseable Success Message')]")
    )
)

driver.execute_script("arguments[0].click();", button)

alert = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,".alert-success")
    )
)

print("Alert Text:",alert.text)

assert "success" in alert.text.lower()

end=time.time()

print("Explicit Wait Time:",round(end-start,2),"seconds")

# ==========================================================
# Sleep Example
# ==========================================================

print("\n========== SLEEP EXAMPLE ==========\n")

driver.refresh()

start = time.time()

button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Autocloseable Success Message')]")
    )
)
button.click()

time.sleep(3)

alert = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Sleep Alert:", alert.text)

end = time.time()

print("Sleep Time:", round(end - start, 2), "seconds")

# ==========================================================
# Clickable Wait
# ==========================================================

print("\n========== CLICKABLE WAIT ==========\n")

driver.refresh()

button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Autocloseable Success Message')]")
    )
)

button.click()

print("Clickable Wait Successful")

# ==========================================================
# Fluent Wait
# ==========================================================

print("\n========== FLUENT WAIT ==========\n")

driver.get("https://testmu.ai/selenium-playground/table-sort-search-demo/")

fluent_wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

rows = fluent_wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr"))
)

print("First Row:")
print(rows[0].text)

# ==========================================================

print("\n====================================")
print("Hands-On 5 Completed Successfully")
print("====================================")

driver.quit()