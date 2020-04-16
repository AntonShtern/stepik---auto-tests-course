import time
from selenium import webdriver
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://www.youtube.com/watch?v=kgGYpmQU1g0&t=1180s")
time.sleep(500)