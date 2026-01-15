from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
#Заходим на страницу
driver.get('https://sky-todo-list.herokuapp.com/')

#Ищем элементы td
tasks = driver.find_elements(By.CSS_SELECTOR, "td_qwer78")
  
#Цикл по таск
for task in tasks:
    print(task.text)

driver.quit()