from selenium.webdriver import Chrome

browser = Chrome()

#browser.set_window_position(400,600)
browser.set_window_size(600,800)
browser.get('https://ya.ru')

rect=browser.get_window_rect()
print(rect.get('x'))
print(rect.get('y'))
print(rect.get('height'))
print(rect.get('width'))
print(rect)

browser.maximize_window()
browser.minimize_window()
browser.fullscreen_window()

browser.quit()