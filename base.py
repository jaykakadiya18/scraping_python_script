from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Firefox()  # or webdriver.Firefox() depending on the browser you're using

# Open a webpage
driver.get("https://www.google.com")

# Find the search box using its name attribute
search_box = driver.find_element(By.NAME, "q")

# Enter text and press Enter
search_box.send_keys("Selenium Python" + Keys.RETURN)

# Wait for some time to view results
time.sleep(5)  # adjust as needed

# Close the browser
driver.quit()
