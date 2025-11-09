from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/dynamic_controls')
form = browser.find_element(By.CSS_SELECTOR, '#input-example')
form.find_element(By.CSS_SELECTOR, 'button').click()

browser.quit()