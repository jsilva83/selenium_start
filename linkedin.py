from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = YOUR LOGIN EMAIL
ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD
PHONE = YOUR PHONE NUMBER

chrome_driver_path = "/Users/angela/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_E=4%2C5%2C6&keywords=enterprise%20architect")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Locate the apply button
time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

# Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
