"""Web automation with Selenium and Python."""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
browser = webdriver.Chrome()
# Navigate to the webpage
browser.get("https://www.github.com")




signin_link = browser.find_element(By.LINK_TEXT, "Sign in") # Find the link to sign in
signin_link.click() # Click the link to sign in