from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/login')
username = browser.find_element(By.CSS_SELECTOR, '#username')
password = browser.find_element(By.CSS_SELECTOR, '#password')

#Проверка, что юзернейм выше чем пароль.

username_y = username.location.get('y')
password_y = password.location.get('y')

if (password_y > username_y): # type: ignore
    print('Полее pass ниже')
else:
    print('Ошибка верстки')

if username.size.get('width') == password.size.get('width'):
    print('Элементы одинаковой ширины')
else:
    print('Ошибка верстки')

browser.quit()