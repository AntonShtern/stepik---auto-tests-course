from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

# pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

import time


def driver():
    options = ChromeOptions()
    options.add_argument("--window-size=800,600")
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install(),
                               options=options,
                               desired_capabilities={'acceptInsecureCerts': True}
                               )
    return browser


def task_1_part11():
    try:
        link1 = "http://suninjuly.github.io/registration1.html"
        link2 = "http://suninjuly.github.io/registration2.html"
        driver_browser = driver()
        # при необходимости поменять на link1
        driver_browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        input1 = driver_browser.find_element_by_tag_name('input')
        input1.send_keys("Ivan")
        input2 = driver_browser.find_element(By.XPATH, '//div[label[contains(., "Last name*")]]/input')
        input2.send_keys("Petrov")
        input3 = driver_browser.find_element(By.XPATH, '//div[label[contains(., "Email*")]]/input')
        input3.send_keys("test@mail.ru")
        button = driver_browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver_browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        driver_browser.quit()


if __name__ == "__main__":
    task_1_part11()
