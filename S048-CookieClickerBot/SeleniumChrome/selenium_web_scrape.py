import json
from selenium import webdriver

# chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

python_url = "https://www.python.org/"

driver.get(python_url)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

events = {n:{"time":event_times[n].text, "name":event_names[n].text} for n in range(len(event_times))}
print(events)

driver.quit()
