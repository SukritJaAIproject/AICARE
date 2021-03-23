# importing webdriver from selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import cv2

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://192.168.1.34:5000/"
# driver = webdriver.Chrome()

while(1):

    driver.get(url)
    driver.save_screenshot("image.png")
    # image = Image.open("image.png")
    img = cv2.imread('image.png')
    cv2.imshow('image', img)
    # driver.close()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

driver.close()