from selenium import webdriver
from selenium.webdriver.common.by import By

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

""" Клик по кнопке с css-классом
1. Открыть страницу http://uitestingplayground.com/classattr
2. Кликнуть на синюю(!) кнопку
3. Запустите скрипт 3 раза. Убедитесь, что код не требуется редактировать – скрипт всегда работает.  """

""" Модальное окно
1. Открыть страницу http://the-internet.herokuapp.com/entry_ad 
2. В модальном окне нажать на кнопку Сlose
3. Выведите в консоль текст элемента с id = content
>Подсказка: тут вам может понадобиться time.sleep(3) """

""" Поле ввода
1. http://the-internet.herokuapp.com/inputs
2. Введите в поле текст 1000
3. Очистите это поле (метод `clear`)
4. введите в это же поле текст 2000 """

""" Форма авторизации
1. Открыть страницу http://the-internet.herokuapp.com/login
2. В поле uername ввести значение *`tomsmith`*
3. В поле password ввести значение *`SuperSecretPassword!`*
4. Нажмите кнопку Login
5. Выведите в консоль текст появившейся зеленой плашки """

""" Переход на Merion Academy
1. Открыть браузер chrome
2. Перейти на страницу google.com
3. В строке поиска написать Merion Academy
4. Нажать Enter (Keys.RETURN)
5. На странице с результатами выбрать первую ссылку и кликнуть на нее
6. После перехода, получить текущий URL:
 - Если URL начинается со строки https://wiki.merionet.ru, написать Добро пожаловать в Merion Academy!.
 - Иначе написать в консоль Мы попали куда-то не туда...  """