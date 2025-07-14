#install newest version of python, and pip (pip is a package manager to install python library)
#pip install selenium
#pip install webdriver-manager

#!!!!!!!!!!!!!!

# To run the script, type in the terminal: python3 scrape_selenium.py
# Also, to run any python file, remember to type in the terminal: python3 <filename.py>

#!!!!!!!!!!!!!!

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 

import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bullsconnect.usf.edu/events?topic_tags=7276307")
time.sleep(40)


event_items = driver.find_elements(By.CLASS_NAME, "list-group-item")


with open("content.txt", "w") as f:
    for item in event_items:
        f.write(item.text)
