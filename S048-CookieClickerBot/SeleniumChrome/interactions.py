from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

# Click on an item using selenium
# article_count.click()

# Selenium has specific find method to click on a link
all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# How do we type "Python" into the search bar?
search_bar = driver.find_element_by_name("search")
search_bar.send_keys("Python")
# Press enter after typing "Python" import keys to use keys that are not of the alphabet
search_bar.send_keys(Keys.ENTER)
