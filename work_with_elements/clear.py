from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/inputs')
element = browser.find_element(By.CSS_SELECTOR, '[type="number"]')
element.send_keys('12345')
element.clear()
element.send_keys('12345')

browser.quit()