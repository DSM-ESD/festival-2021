from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path = 'C:/Users/DSM/Desktop/study/chromedriver_win32/chromedriver.exe')
driver.get("https://handson.ga/index.html")
search = driver.find_element_by_css_selector("input[type='file']").send_keys(r"C:/Users/DSM/Desktop/study/hand.jpg")
time.sleep(2)
a = driver.find_elements_by_class_name("son-label d-flex align-items-center")

result = driver.find_elements_by_class_name("d-block percent-text")
print(result)
