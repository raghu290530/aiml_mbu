from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# -----------------------------------
# 1. Open Chrome
# -----------------------------------

driver = webdriver.Chrome()

driver.maximize_window()

time.sleep(2)


# -----------------------------------
# 2. Open Selenium practice website
# -----------------------------------

driver.get("https://the-internet.herokuapp.com/")

time.sleep(2)


# -----------------------------------
# 3. Go to Inputs page
# -----------------------------------

driver.get("https://the-internet.herokuapp.com/inputs")

time.sleep(2)

print("Opened Inputs page")


# Find the input box
input_box = driver.find_element(By.TAG_NAME, "input")

# Enter a value
input_box.send_keys("12345")

time.sleep(2)

print("Entered value:", input_box.get_attribute("value"))


# -----------------------------------
# 4. Move to Add/Remove Elements
# -----------------------------------

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

time.sleep(2)

print("Moved to Add/Remove page")


# Click Add Element
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

add_button.click()

time.sleep(2)

print("Clicked Add Element")


# Find Delete button
delete_button = driver.find_element(
    By.XPATH,
    "//button[text()='Delete']"
)

print("Delete button found")


# Click Delete
delete_button.click()

time.sleep(2)

print("Clicked Delete")


# -----------------------------------
# 5. Move to Dropdown page
# -----------------------------------

driver.get("https://the-internet.herokuapp.com/dropdown")

time.sleep(2)

print("Moved to Dropdown page")


# Find dropdown
dropdown = driver.find_element(By.ID, "dropdown")

# Select Option 2
select = Select(dropdown)

select.select_by_visible_text("Option 2")

time.sleep(2)

print("Selected Option 2")


# -----------------------------------
# 6. Move to Dynamic Loading
# -----------------------------------

driver.get(
    "https://the-internet.herokuapp.com/dynamic_loading/2"
)

time.sleep(2)

print("Moved to Dynamic Loading page")


# Click Start
start_button = driver.find_element(
    By.CSS_SELECTOR,
    "#start button"
)

start_button.click()

print("Clicked Start")


# Wait until Hello World appears
message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.ID, "finish")
    )
)

print("Dynamic result:", message.text)


# -----------------------------------
# 7. Close browser
# -----------------------------------

time.sleep(3)

driver.quit()

print("Automation completed")