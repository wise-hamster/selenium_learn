from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#Заходим на страницу
driver.get('https://the-internet.herokuapp.com/login')

#Поиск элемента и добавление текста
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')

#Поиск элемента и добавление текста
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
#Поиск кнопки и клик по ней
driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
#Поиск текста и сохранение в переменную.
txt = driver.find_element(By.CSS_SELECTOR,'#flash').text
print(txt)

driver.quit()