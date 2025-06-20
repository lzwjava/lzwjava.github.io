from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up Chrome driver
service = Service(executable_path="/usr/bin/chromedriver")  # Replace with the actual path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the URL
driver.get("https://grok.com/")

# Print the title of the page
print("Title of the page:", driver.title)

# Close the driver
driver.quit()