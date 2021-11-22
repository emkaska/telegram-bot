import os
import datetime
import logging
import time
from selenium import webdriver
from PIL import Image

def crop_image(link, filename='table.png'):
    try:
        driver = webdriver.Chrome("chromedriver.exe")
        url = link
        driver.get(url)
        driver.execute_script("document.body.style.zoom='50%'")
        driver.set_window_size(1920, 1080, driver.window_handles[0])
        driver.maximize_window()
        time.sleep(5)
        driver.save_screenshot(filename)
        print('Screen Captured')
        
    except Exception as e:
        logging.error(str(e))
    return filename