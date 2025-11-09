from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/')
texts = browser.find_elements(By.CSS_SELECTOR, '#content a')
texts = browser.find_elements(By.CSS_SELECTOR, '#content li')

locato_text_links = {'a': [text.text for text in texts], 'li': [text.text for text in texts]}

print(locato_text_links)
browser.quit()