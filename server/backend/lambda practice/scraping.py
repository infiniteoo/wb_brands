
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.by import By
import csv
import requests

from selenium.webdriver.edge.service import Service

service = Service(executable_path="C:\edge_driver\msedgedriver.exe")
options = webdriver.EdgeOptions()

driver = webdriver.Edge(service=service, options=options)

# Open a webpage
parent_folder="hbo"
driver.get("https://hbo.com/")



# Example of extracting data from the page
links = [element.get_attribute('href') for element in driver.find_elements(By.TAG_NAME, 'a')]

print(links)

       
            

for index, link in enumerate(links):
   
  
    if link:
        driver.get(link)
        time.sleep(5)
        os.makedirs('data', exist_ok=True)
        folder_name = f"link_{index}"
        os.makedirs(os.path.join('data',parent_folder), exist_ok=True)    
        os.makedirs(os.path.join('data',f'{parent_folder}', 'images', folder_name), exist_ok=True)

        text_dir = os.path.join('data',f'{parent_folder}', 'text')
        os.makedirs(text_dir, exist_ok=True)    
        page_title = driver.title
        print(page_title)
        page_url = driver.current_url
        print(page_url)
        # Write to CSV
        with open('extracted_data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([page_title, page_url])
         # Extract text
        all_text = driver.find_element(By.TAG_NAME, "body").text

        # Save text to a file
        text_file_path = os.path.join(text_dir, f'text_{index}.txt')
        with open(text_file_path, 'w', encoding='utf-8') as file:
            file.write(all_text)

        # Extract image URLs
        image_elements = driver.find_elements(By.TAG_NAME, "img")
        image_urls = [img.get_attribute('src') for img in image_elements]

        for img_index, img in enumerate(image_elements):
            img_url = img.get_attribute('src')
            if img_url:
                try:
                    img_data = requests.get(img_url).content
                    img_file_path = os.path.join('data', f'{parent_folder}','images', folder_name, f'image_{img_index}.jpg')
                    with open(img_file_path, 'wb') as img_file:
                        img_file.write(img_data)
                except Exception as e:
                    print(f"Error downloading {img_url}: {e}")

# Close the browser
driver.quit()
