from selenium.webdriver import Chrome

browser = Chrome()
browser.get('https://ya.ru')

browser.save_screenshot('ya.png')