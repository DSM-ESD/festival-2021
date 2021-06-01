from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://handson.ga/")
a = driver.find_element_by_class_name("file-upload-input")
#driver.find_element_by_css_selector("input[type='file']").send_keys(r"/Users/kimminyoung/Desktop/workspace/crawler/test.jpeg")
#test = driver.find_element_by_css_selector('input[type="file"]')
print('1')
print(a)
a = a.send_keys(r"/Users/kimminyoung/Desktop/workspace/crawler/test.jpeg")
#test.send_keys(r'/Users/kimminyoung/Desktop/workspace/crawler/test.jpeg')
print(a)
print('2s')
driver.close()
