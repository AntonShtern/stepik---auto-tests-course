from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    browser.execute_script("window.scrollBy(0, 100);") # скролл
    
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    #
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    #Button
    browser.find_element_by_tag_name("button").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла 224592