from selenium import webdriver
import time
import math

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение для Х и вычислям значение у
    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    # Находим поле для ввода и записываем туда значение у
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()
    
    input3 = browser.find_element_by_id("robotsRule")
    input3.click()

    button1 = browser.find_element_by_tag_name("button")
    button1.click()
    
    
    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    


    # robots_radio = browser.find_element_by_id("robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # print("value of robot's radio: ", robots_checked)
    # assert robots_checked is not None, "Robots radio is not selected by default"
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла 224592