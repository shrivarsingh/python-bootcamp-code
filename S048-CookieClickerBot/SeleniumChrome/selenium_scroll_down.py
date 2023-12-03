from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# CHROME_DRIVER_PATH = "C:\Development\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome()

driver.get("https://www.google.com")
search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.send_keys("kitten")
search.send_keys(Keys.ENTER)
time.sleep(10)
images = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
images.click()
time.sleep(10)
page = driver.find_element_by_css_selector("body")
page.send_keys(Keys.END)
