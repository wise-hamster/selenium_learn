from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#Open Chrome browser
browser = Chrome()
#Get to URL
browser.get('https://the-internet.herokuapp.com/javascript_alerts')

#Find element
browser.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
#Switching to alert
alert = browser.switch_to.alert
#Print value alert
print(alert.text)
#Click to OK
alert.accept()

#Find element and ckick
browser.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
#Switching to alert and click to Cancel
browser.switch_to.alert.dismiss()

#Find element and ckick
browser.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
#Switching to alert and click to Okay
browser.switch_to.alert.accept()

#Find element and ckick
browser.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
#Switching to alert and send text
alert = browser.switch_to.alert
alert.send_keys('test 42')
alert.accept()

#Close Chrome driver
browser.quit()
