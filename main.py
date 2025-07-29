from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Optional: use this if chromedriver is in your PATH, or specify path directly
driver = webdriver.Chrome()

# Open the sign-up page
driver.get("https://oneamazingreport.com/signup")

# Maximize window to reduce chance of overlays
driver.maximize_window()

# Wait for elements to load
wait = WebDriverWait(driver, 10)

# Fill First Name
first_name = wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
first_name.send_keys("John")

# Fill Last Name
last_name = driver.find_element(By.NAME, "last_name")
last_name.send_keys("Doe")

# Fill Email
email = driver.find_element(By.NAME, "work_email")
email.send_keys("john.doe@example.com")

# Fill Password
password = driver.find_element(By.NAME, "password")
password.send_keys("StrongPass123!")

# Fill Confirm Password
confirm_password = driver.find_element(By.NAME, "password_confirmation")
confirm_password.send_keys("StrongPass123!")

# Locate the Submit Button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign up")]')))

# Scroll to the button
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
time.sleep(1)  # Let any animation/overlay complete

# Click using JS to avoid overlay issue
driver.execute_script("arguments[0].click();", submit_button)

# Optional: wait to see result
time.sleep(5)

# Close the browser
driver.quit()
