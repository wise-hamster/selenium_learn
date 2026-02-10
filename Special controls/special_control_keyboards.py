from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')

ActionChains(driver)\
    .key_down(Keys.CONTROL)\
    .send_keys('a')\
    .send_keys('с')\
    .key_up(Keys.CONTROL)\
    .perform()    
input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
chain = ActionChains(driver)
chain.send_keys_to_element(input,'Selenium')\
    .key_down(Keys.LEFT_SHIFT)\
    .send_keys(Keys.ARROW_UP)\
    .key_up(Keys.LEFT_SHIFT)\
    .pause(3)\
    .key_down(Keys.CONTROL)\
    .send_keys('xvvvvv')\
    .perform()
    

driver.quit()