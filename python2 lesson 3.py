from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


try: 
    browser.find_element_by_name("firstname").send_keys('Вася')
    browser.find_element_by_name("lastname").send_keys('Васев')
    browser.find_element_by_name("email").send_keys('Вася@com')

    current_dir = os.path.abspath(os.path.dirname( "C:/Users/User/Desktop/test/file1.txt "))
    #print('путь к папке = ', current_dir)
    file_path = os.path.join(current_dir, 'file1.txt')
    #print('путь к файлу = ', file_path)
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_tag_name("button").click()
    # current_dir = os.path.abspath(os.path.dirname("python2 lesson2 step5.py"))    # получаем путь к директории текущего исполняемого файла 
    # file_path = os.path.join(current_dir, 'python2 lesson2 step5.py')           # добавляем к этому пути имя файла 
    # element.send_keys(file_path)
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла 224592