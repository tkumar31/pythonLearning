from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open a website
driver.get("https://www.google.com")

# Find an element (e.g., the search box) and perform an action
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium with Python")
search_box.submit()

# Close the driver
driver.quit()