from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/dynamic_controls')

browser.find_element(By.CSS_SELECTOR,'[type=checkbox]').click() # - > 1 элемент  == $()
browser.find_element(By.CSS_SELECTOR,'[onclick="swapCheckbox()"]').click()
browser.get('https://the-internet.herokuapp.com/inputs')
browser.find_element(By.CSS_SELECTOR, '[type="number"]').send_keys('12345')

browser.get('https://2048game.com/ru/')
body_game = browser.find_element(By.CSS_SELECTOR, 'body')
for x in range(1000):
    body_game.send_keys(Keys.ARROW_DOWN)
    body_game.send_keys(Keys.ARROW_LEFT)
    body_game.send_keys(Keys.ARROW_UP)
    body_game.send_keys(Keys.ARROW_RIGHT)

browser.quit()