from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# Set up Firefox options
firefox_options = Options()
# firefox_options.add_argument("--headless")  # Optional: Remove for visible browser

# Specify the default profile path
profile_path = "/home/lzw/Downloads/sele"  # Adjust based on profiles.ini
firefox_profile = FirefoxProfile(profile_path)
firefox_options.profile = firefox_profile
firefox_options.log.level = "trace"

# Set up geckodriver service
service = Service(executable_path="/home/lzw/bin/geckodriver")  # Adjust if geckodriver is elsewhere
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open the URL
driver.get("https://grok.com/")

# Print the title of the page
print("Title of the page:", driver.title)

# Close the driver
driver.quit()