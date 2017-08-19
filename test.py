from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Webdrivers\chromedriver.exe")
options = webdriver.ChromeOptions()

# driver can be given in path
driver.get("https://google.com")
driver.maximize_window()
time.sleep(3)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(3)
driver.quit()

# start with custom profile
# start maximized
# executable in a nin standard location
# might be needed for arguments
