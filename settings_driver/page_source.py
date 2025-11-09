from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://ya.ru')

print(driver.page_source)

driver.quit()