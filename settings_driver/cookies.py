from selenium.webdriver import Chrome

browser = Chrome()
browser.get('https://trello.com/')
token = ''

my_cookie = {"name": 'cloud.session.token',
             'value': token}

browser.add_cookie(my_cookie)
browser.refresh()

#print(browser.get_cookies())
print(browser.get_cookie("cloud.session.token"))
browser.delete_all_cookies()

browser.refresh()
browser.quit()