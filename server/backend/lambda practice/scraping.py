
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

linkData = ["discoveryplus", "tbs", "foodnetwork", "tntdrama", "investigatondiscovery", "tlc", "dccomics", "eurosport", "cookingchanneltv", "warnerbrosgames", "animalplanet", "discoverysports", "adultswim", "cartoonnetwork", "golfdigest", "travelchannel", "hogarhgtv", "onefifty", "discoveryenespanol", "trutv", "cinemax", "motortrendondemand", "sciencechannel", "ahctv", "asianfoodnetwork", "bleacherreport", "destinationamerica", "tntsports", "tcm", "discoveryfamilychannel", "boomerang", "discoveryfamilia", "discoverylife", "cnnespanol.cnn", "roosterteeth","warnerbros"]

specificLinks = ["oprah.com/app/own-tv.html", "warnerbros.com/company/divisions/television", "warnerbros.com/company/divisions/motion-pictures", "magnolia.com/network", "discoverysports.com/page/about-warner-bros-discovery-sports", "warnerbros.com/company/divisions/motion-pictures", "www.cnn.com/specials/videos/hln", "discoveryplus.co.uk/channels/quest-red", "discoveryplus.com/gb/channel/quest", "www.cartoonnetwork.com/cartoonito/", "www.tvn.pl/", "dmax.de/", "realtime.it/", "giallotv.it/", "nove.tv/", "discoveryplus.com/fi/channel/frii", "frisbeetv.it/", "www.k2tv.it/", "discoverydenmark.dk/", "tntgo.tv/", "tabichan.jp/", "pogo.tv/index.html", "mondotv.jp/", "tooncast.tv/", "boingtv.it/", "warnertv.de/"]

twitterHandles = ["truTV", "StreamOnMax", "HBO", "Warnerbros", "hgtv", "TBSNetwork", "CNN", "discoveryplus", "Discovery", "FoodNetwork", "tntdrama", "OWNTV", "DiscoveryID", "wbpictures", "warnerbrostv", "DCComics", "TLC", "eurosport", "magnolianetwork", "CookingChannel", "wbgames", "adultswim", "discoverysports", "AnimalPlanet", "HLNTV", "cartoonnetwork", "newlinecinema", "GolfDigest", "thisisonefifty", "travelchannel", "CartoonitoCN", "Cinemax", "MotorTrend", "BleacherReport", "ahc_tv", "ScienceChannel", "DestAmerica", "TNTSportsAR", "tcm", "discoveryfamily", "realtimetvit", "DMAX_TV", "BoomerangToons", "nove", "tabichanjp", "discoveryfam", "disclifechannel", "mondotvjp", "WarnerBrosTVDE", "CNNee", "RoosterTeeth"]

for link in linkData:
    parent_folder = link
    driver.get(f"https://{link}.com/")
    time.sleep(3)

    links = [element.get_attribute('href') for element in driver.find_elements(By.TAG_NAME, 'a')]

    # remove any links with "javascript" in them

    for link in links:
        """ if "javascript" in link:
          links.remove(link)

        if "cross-device-privacy" in link:
            links.remove(link) """




    print(links)

       
            

    for index, link in enumerate(links):
    
    
        if link:
            driver.get(link)
            time.sleep(5)
            os.makedirs('data', exist_ok=True)
            folder_name = f"link_{index}"
            os.makedirs(os.path.join('data',parent_folder), exist_ok=True)    
            # os.makedirs(os.path.join('data',f'{parent_folder}', 'images', folder_name), exist_ok=True)

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

            # Extract image URLs - abandoned 
            """ image_elements = driver.find_elements(By.TAG_NAME, "img")
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
                        print(f"Error downloading {img_url}: {e}") """

    # Close the browser
    driver.quit()
