from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)




button1 = browser.find_element_by_tag_name("button")
button1.click()
assert True