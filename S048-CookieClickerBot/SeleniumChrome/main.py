from selenium import webdriver

# chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome()


python_url = "https://www.python.org/"

driver.get(python_url)

# amazon_url
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# python_url
search_bar = driver.find_element_by_name("q")
print()
print(search_bar)
print()
print(search_bar.tag_name)
print()
print(search_bar.get_attribute("placeholder"))
print()
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print()
print(documentation_link.text)
# Find by Xpath
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print()
print(bug_link.text)
# Select multiple elements we use plural - driver.find_elements_by_css_selector("")
print("\nDone")


# driver.close()  # closes a single tab
driver.quit()  # closes the entire browser