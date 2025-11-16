from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://ya.ru/')

element = browser.find_element(By.CSS_SELECTOR, '#text')
print(element.get_dom_attribute('aria-controls'))# return value
print(element.get_dom_attribute('not_exists'))# None
print(element.get_dom_attribute('autofocus')) # true

print(element.get_property('namespaceURI'))# return value
print(element.get_property('not_exists'))# None
print(element.get_property('autofocus')) # True

print(element.get_attribute('namespaceURI'))
print(element.get_attribute('aria-controls'))
print(element.get_attribute('autofocus'))
print(element.get_attribute('not_exists'))


browser.quit()

