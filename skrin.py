import pyautogui

x = pyautogui.screenshot()
x.save('my_skrin.png')


# import PIL.ImageGrab

# im = PIL.ImageGrab.grab()
# im.show()
# from selenium import webdriver
# from PIL import Image
# driver = webdriver.Chrome(executable_path = 'C://Users/Jomok/Desktop').encoding="utf-8"
# url = "https://www.google.com/"
# driver.get(url)
# driver.save_screenshot('ss.png')
# screenshot = Image.open('ss.png')
# screenshot.show()

# from selenium import webdriver
# # import time
# driver=webdriver.Firefox()
# driver.get("https://www.google.co.in")
# driver.implicitly_wait(2)
# driver.save_screenshot("C:/Users/Jomok/Desktop/test.png")
# driver.quit()

from base64 import b64decode
from wand.image import Image
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
# import math

# def get_element_screenshot(element: x) -> bytes:
#     driver = element._parent
#     ActionChains(driver).move_to_element(element).perform()  # focus
#     src_base64 = driver.get_screenshot_as_base64()
#     scr_png = b64decode(src_base64)
#     scr_img = Image(blob=scr_png)

#     x = element.location["200"]
#     y = element.location["150"]
#     w = element.size["width"]
#     h = element.size["height"]
#     scr_img.crop(
#         left=math.floor(x),
#         top=math.floor(y),
#         width=math.ceil(w),
#         height=math.ceil(h),
#     )
#     return scr_img.make_blob()