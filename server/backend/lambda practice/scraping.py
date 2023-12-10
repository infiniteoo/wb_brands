
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.edge.service import Service

service = Service(executable_path="C:\edge_driver\msedgedriver.exe")
options = webdriver.EdgeOptions()

driver = webdriver.Edge(service=service, options=options)

# Open a webpage
#driver.get("https://wbd.com/our-brands/")
driver.get("https://hbo.com/")

# You might need to wait for the page to load or for certain elements to become available
time.sleep(5)  # Waits for 5 seconds

# Example of extracting data from the page
links = [element.get_attribute('href') for element in driver.find_elements(By.TAG_NAME, 'a')]

print(links)
with open('extracted_data.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for link in links:
        if link:
            driver.get(link)
            time.sleep(5)
            # Extract specific data here
            page_title = driver.title
            page_url = driver.current_url
            # Write to CSV
            writer.writerow([page_title, page_url])



# Close the browser
driver.quit()
