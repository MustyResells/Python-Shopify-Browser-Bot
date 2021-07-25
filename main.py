from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome Drivers
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Opening site
driver.get("product link here")
print(driver.title)

#Login Email
search = driver.find_element_by_name("add")

#Send Email
search.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

search = driver.find_element_by_name("checkout")

search.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

search = driver.find_element_by_name("checkout[email]")

search.send_keys("your email here")

search = driver.find_element_by_name("checkout[shipping_address][first_name]")

search.send_keys("first name here")

search.send_keys(Keys.RETURN)

search = driver.find_element_by_name("checkout[shipping_address][last_name]")

search.send_keys("last name here")

search = driver.find_element_by_name("checkout[shipping_address][address1]")

search.send_keys("address 1 here")

search.send_keys(Keys.RETURN)

search = driver.find_element_by_name("checkout[shipping_address][city]")

search.send_keys("town / city here")

search.send_keys(Keys.RETURN)

search = driver.find_element_by_name("checkout[shipping_address][zip]")

search.send_keys("zip / postal code here")

search.send_keys(Keys.RETURN)

driver.implicitly_wait(5000)

search = driver.find_element_by_id("continue_button")

search.send_keys(Keys.RETURN)

search = driver.find_element_by_id("number")

search.send_keys("card #")

search.send_keys(Keys.RETURN)

search = driver.find_element_by_name("name")

search.send_keys("name on card")

search.send_keys(Keys.RETURN)

search = driver.find_element_by_name("expiry")

search.send_keys("card expiry")

search.send_keys(Keys.RETURN)
