import pytest  # type: ignore

# Some linters/IDE environments may not resolve selenium imports; silence them
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait, Select  # type: ignore


# ------------------------------
# Task 1
# ------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.ID,"user-message"))
    )

    message_box = driver.find_element(By.ID,"user-message")
    message_box.clear()
    message_box.send_keys(message)

    driver.find_element(By.ID,"showInput").click()

    output = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.ID,"message"))
    )

    assert output.text == message


# ------------------------------
# Task 2
# ------------------------------

def test_checkbox_demo(driver, base_url):

    driver.get(base_url + "checkbox-demo")

    checkbox = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    driver.execute_script("arguments[0].click();", checkbox)

    assert checkbox.is_selected()

    driver.execute_script("arguments[0].click();", checkbox)

    assert not checkbox.is_selected()


# ------------------------------
# Task 3
# ------------------------------

def test_dropdown_selection(driver, base_url):

    driver.get(base_url + "select-dropdown-demo")

    dropdown = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
            (By.ID,"select-demo")
        )
    )

    select = Select(dropdown)

    select.select_by_visible_text("Wednesday")

    selected = select.first_selected_option.text

    assert selected == "Wednesday"