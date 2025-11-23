from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

""" Клик по кнопке
1. Открыть страницу http://the-internet.herokuapp.com/add_remove_elements/
2. 5 раз кликнуть на кнопку Add Element
3. Собрать со страницы список кнопок Delete
4. Вывести на экран размер списка """
browser = webdriver.Chrome()
browser.get('http://the-internet.herokuapp.com/add_remove_elements/')

clicker = browser.find_element(By.CSS_SELECTOR, '#content > div > button')
text = clicker.text
for x in range(5):
    clicker.click()
    print(f'{x+1} click "{text}"')

list_delete = browser.find_elements(By.CSS_SELECTOR,'#elements .added-manually')
delete_text = browser.find_element(By.CSS_SELECTOR,'#elements .added-manually').text
print(f'{len(list_delete)} "{delete_text}"')

browser.quit()

""" Клик по кнопке без id
1. Открыть страницу http://uitestingplayground.com/dynamicid
2. Кликнуть на синюю кнопку
3. Запустите скрипт 3 раза. Убедитесь, что код не требуется редактировать – скрипт всегда работает.  """
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

btn = driver.find_element(By.CSS_SELECTOR, ".btn[type=button]")
btn.click()
driver.quit()

""" Клик по кнопке с css-классом
1. Открыть страницу http://uitestingplayground.com/classattr
2. Кликнуть на синюю(!) кнопку
3. Запустите скрипт 3 раза. Убедитесь, что код не требуется редактировать – скрипт всегда работает.  """
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
btn.click()
driver.quit()

""" Модальное окно
1. Открыть страницу http://the-internet.herokuapp.com/entry_ad 
2. В модальном окне нажать на кнопку Сlose
3. Выведите в консоль текст элемента с id = content
>Подсказка: тут вам может понадобиться time.sleep(3) """
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")
time.sleep(3)
close = driver.find_element(By.CSS_SELECTOR, "#modal .modal-footer")
close.click()
content = driver.find_element(By.CSS_SELECTOR, "#content").text
print(content)
driver.quit()

""" Поле ввода
1. http://the-internet.herokuapp.com/inputs
2. Введите в поле текст 1000
3. Очистите это поле (метод `clear`)
4. введите в это же поле текст 2000 """
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/inputs")
element = driver.find_element(By.CSS_SELECTOR, '.example [type="number"]')
element.send_keys('1000')
element.clear()
element.send_keys('2000')
driver.quit()

""" Форма авторизации
1. Открыть страницу http://the-internet.herokuapp.com/login
2. В поле uername ввести значение *`tomsmith`*
3. В поле password ввести значение *`SuperSecretPassword!`*
4. Нажмите кнопку Login
5. Выведите в консоль текст появившейся зеленой плашки """
driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/login')
login = driver.find_element(By.CSS_SELECTOR, '#username')
login.send_keys('tomsmith')
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('SuperSecretPassword!')
button = driver.find_element(By.CSS_SELECTOR, '#login > button > i').click()
time.sleep(2)
result = driver.find_element(By.CSS_SELECTOR, '#flash-messages').text
print(result)
driver.quit()

""" Переход на Merion Academy
1. Открыть браузер chrome
2. Перейти на страницу google.com
3. В строке поиска написать Merion Academy
4. Нажать Enter (Keys.RETURN)
5. На странице с результатами выбрать первую ссылку и кликнуть на нее
6. После перехода, получить текущий URL:
 - Если URL начинается со строки https://wiki.merionet.ru, написать Добро пожаловать в Merion Academy!.
 - Иначе написать в консоль Мы попали куда-то не туда...  """

driver = webdriver.Chrome()
driver.get('http://google.com')
search_merion = driver.find_element(By.CSS_SELECTOR, '.YacQv')
search_merion.send_keys('Merion Academy')
search_merion.send_keys(Keys.RETURN)
driver.find_element(By.CSS_SELECTOR, "h3").click()

if driver.current_url.startswith("https://wiki.merionet.ru"):
    print("Добро пожаловать в Merion Academy!")
else:
    print("Мы попали куда-то не туда...")
    
driver.quit()