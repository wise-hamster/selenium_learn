from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

#Open Chrome browser
browser = Chrome()
#Get to URL
browser.get('https://the-internet.herokuapp.com/windows')
browser.get('https://ya.ru')

# Go to back page
browser.back()

# Go to forward page
browser.forward()

# Go to back page
browser.back()

# Go to forward page
browser.refresh()

#The value of the title
title = browser.title
print(title)

#Current URL
url = browser.current_url
print(url)

#Find element
browser.find_element(By.CSS_SELECTOR, value = 'a[href="/windows/new"]').click()

#Close Chrome windows
browser.close()

#Close Chrome driver
browser.quit()