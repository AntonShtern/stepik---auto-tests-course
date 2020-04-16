from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()
url = 'http://example.com/usersignin'
changed_url = 'https://example.com/userwelcome'

browser.get(url)

wait = WebDriverWait(browser, 10)
status = wait.until(ec.url_changes(changed_url))
print(status)