import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Check command-line arguments
if len(sys.argv) < 6:
    print("Usage: python bot.py <first_name> <last_name> <email> <password> <confirm_password>")
    sys.exit(1)

first_name_val = sys.argv[1]
last_name_val = sys.argv[2]
email_val = sys.argv[3]
password_val = sys.argv[4]
confirm_password_val = sys.argv[5]

# Initialize Chrome WebDriver (make sure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

try:
    # Open the sign-up page
    driver.get("https://oneamazingreport.com/signup")

    # Maximize window
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Fill First Name
    first_name = wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
    first_name.send_keys(first_name_val)

    # Fill Last Name
    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys(last_name_val)

    # Fill Email
    email = driver.find_element(By.NAME, "work_email")
    email.send_keys(email_val)

    # Fill Password
    password = driver.find_element(By.NAME, "password")
    password.send_keys(password_val)

    # Fill Confirm Password
    confirm_password = driver.find_element(By.NAME, "password_confirmation")
    confirm_password.send_keys(confirm_password_val)

    # Locate the Submit Button
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign up")]')))

    # Scroll to the button
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Wait for any animation/overlay

    # Click submit button via JS (to avoid overlay issues)
    driver.execute_script("arguments[0].click();", submit_button)

    # Wait for some time to observe result or page load
    # time.sleep(5)
    time.sleep(5)

finally:
    # Close browser
    # driver.quit()
    pass  
