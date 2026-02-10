from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" 
Нажатие на кнопку
1. Перейти на страницу http://uitestingplayground.com/ajax
2. Нажать на синюю кнопку
3. Получить текст из зеленой плашки
4. Вывести его в консоль (”Data loaded with AJAX get request.”) """

driver = webdriver.Chrome()
waiter = WebDriverWait(driver,60)
driver.get('http://uitestingplayground.com/ajax')
button_triggering_AJAX_request = driver.find_element(By.CSS_SELECTOR,'#ajaxButton')
button_triggering_AJAX_request.click()
success_element = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.bg-success')))
print(success_element.text)
driver.quit()

""" Переименовать кнопку
Шаги:
1. Перейти на сайт http://uitestingplayground.com/textinput
2. Указать в поле ввода текст "Merion"
3. Нажать на синюю кнопку
4. Получить текст кнопки и вывести в консоль (Merion) """

driver = webdriver.Chrome()
waiter = WebDriverWait(driver,60)
driver.get('http://uitestingplayground.com/textinput')

text_place = driver.find_element(By.CSS_SELECTOR,'#newButtonName').send_keys('Marion')
button_rename = driver.find_element(By.CSS_SELECTOR,'#updatingButton').click()
success_element = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#updatingButton'))) 

print(success_element.text)
driver.quit()

""" Дождаться картинки
Шаги:
1. Перейти на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
2. Дождаться загрузки всех картинок
3. Получить значение атрибута src у 3й картинки
4. Вывести значение в консоль """

driver = webdriver.Chrome()
waiter = WebDriverWait(driver,60)
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#compass')))
waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#calendar')))
element = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#award')))
waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#calendar')))

src_value = element.get_attribute("src")
print(src_value)
driver.quit()

""" 
Скрипт заполнения формы 
Шаги:
1. Открыть страницу https://bonigarcia.dev/selenium-webdriver-java/data-types.html
2. Заполнить форму значениями   
3. Нажать кнопку Submit
4. Вывести в консоль цвет полей Zip code, E-mail и Phone (background-color) """

form_value = form_data = {"first_name": "Иван","last_name": "Петров","address": "Ленина, 55-3",
    "zip_code": "","city": "Москва","country": "Россия","e-mail": "","phone_number": "",
    "job_position": "QA","Company": "Merion"}
driver = webdriver.Chrome()
driver.implicitly_wait(10)
waiter = WebDriverWait(driver,60)
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

driver.find_element(By.CSS_SELECTOR, "input.form-control[name='first-name']").send_keys(str(form_value.get('first_name')))
driver.find_element(By.CSS_SELECTOR, "input.form-control[name='last-name']").send_keys(str(form_value.get('last_name')))
driver.find_element(By.CSS_SELECTOR, "input.form-control[name='address']").send_keys(str(form_value.get('address')))
driver.find_element(By.CSS_SELECTOR, "input.form-control[name='city']").send_keys(str(form_value.get('city')))
driver.find_element(By.CSS_SELECTOR, "input.form-control[name='job-position']").send_keys(str(form_value.get('job_position')))
driver.find_element(By.CSS_SELECTOR, "input.form-control[name='company']").send_keys(str(form_value.get('company')))
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property('background-color')
e_mail = driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property('background-color')
phone = driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property('background-color')

print(zip_code , e_mail, phone, sep = '\n')
driver.quit()

""" 
Скрипт на калькулятор
Шаги:
1. Открыть страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
2. В поле ввода по локатору #delay ввести значение 45
3. Нажать на кнопки
    1. 7
    2. + (плюс)
    3. 8
    4. =
4. Дождаться результата. Вывести его в консоль."""

driver = webdriver.Chrome()
waiter = WebDriverWait(driver,60)
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

driver.find_element(By.CSS_SELECTOR, '#delay').clear()
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'),'15'))

element = driver.find_element(By.CSS_SELECTOR,'.screen').text
print(element)


""" Напишите скрипт для работы с интернет-магазином. Шаги

1. Открыть сайт магазина https://www.saucedemo.com/
2. Авторизоваться под пользователем standard_user
3. Добавить в корзину товары:
    1. Sauce Labs Backpack
    2. Sauce Labs Bolt T-Shirt 
    3. Sauce Labs Onesie
4. Перейти в корзину
5. Нажать Checkout
6. Заполнить форму данными:
    1. Имя
    2. Фамиля
    3. Почтовый индекс
7. Нажать continue
7. Прочитать со стрницы итоговую стоимость ( Total )
8. Закрыть браузер
9. Вывести в консоль итоговую стоимость """

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://www.saucedemo.com/')

#authorization
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys ('standard_user')
driver.find_element(By.CSS_SELECTOR, "#password").send_keys ('secret_sauce')
driver.find_element(By.CSS_SELECTOR, '#login-button').click()

#add to cart
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()


driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
driver.find_element(By.CSS_SELECTOR, '#checkout').click()

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Viktor')
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Polivenko')
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, '#continue').send_keys('123456')
total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label')
print(total.text)
#checkout_summary_container > div > div.summary_info > div.summary_total_label
driver.quit()