from selenium import webdriver
import time

drv = webdriver.Chrome("D:\Raman\chromedriver_win32\chromedriver.exe")
print(drv)
drv.get('https://www.facebook.com/')

drv.find_element_by_id('email').send_keys('xyz@gmail.com')
drv.find_element_by_id('pass').send_keys('test')

drv.find_element_by_id('pass').submit()
