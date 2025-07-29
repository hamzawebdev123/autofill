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

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://oneamazingreport.com/signup")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Wait for the slot status to load (adjust selector below based on actual HTML)
    try:
        slot_status = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Slot Available')]")))
        if "available" in slot_status.text.lower():
            print("✅ Slot is available. Proceeding to autofill...")

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
            time.sleep(1)

            # Click the button using JS
            driver.execute_script("arguments[0].click();", submit_button)

            time.sleep(5)  # Wait for result
        else:
            print("❌ Slot not available. Aborting autofill.")
    except Exception as e:
        print("⚠️ Could not detect slot availability or an error occurred:", str(e))

finally:
    driver.quit()
