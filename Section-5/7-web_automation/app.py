"""Web automation with Selenium and Python."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Create a new instance of the Firefox driver
browser = webdriver.Chrome()
# Navigate to the webpage
browser.get("https://www.github.com")




signin_link = browser.find_element(By.LINK_TEXT, "Sign in") # Find the link to sign in
signin_link.click() # Click the link to sign in

username = browser.find_element(By.ID, "login_field") # Find the username field
username.send_keys("your username") # Enter your username
password = browser.find_element(By.ID, "password") # Find the password field
password.send_keys("your password") # Enter your password
password.submit() # Submit the form

    # Wait for a few seconds to observe the result (optional)
time.sleep(1000)

