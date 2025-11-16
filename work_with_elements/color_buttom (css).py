from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/login')

button = browser.find_element(By.CSS_SELECTOR, ('.radius'))
value = button.value_of_css_property('background-color')


if value == 'rgba(43, 166, 203, 1)':
    print('Color correct')
else:
    print('UI error')