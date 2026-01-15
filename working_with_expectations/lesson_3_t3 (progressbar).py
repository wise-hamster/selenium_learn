from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/progressbar')
waiter = WebDriverWait(driver,60, 0.1)
text_to_be = '75%'

driver.find_element(By.CSS_SELECTOR, "#startButton").click()
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#progressBar'),text_to_be))
driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

driver.quit()