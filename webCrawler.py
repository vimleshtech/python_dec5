from selenium import webdriver
import time

drv = webdriver.Chrome("D:\Raman\chromedriver_win32\chromedriver.exe")
print(drv)
drv.get('https://www.google.com/')

'''
WebElement Locator:find html web element

find_element_by_id
find_element_by_name

find_element_by_class

find_element_by_xpath (location)

find_element_by_linktext 

find_element_by_tag_name


    
'''

el = drv.find_element_by_name('q')
el.send_keys("python example")
el.submit()

#wait for 5 seconds
time.sleep(5)

#get data from web page
#//*[@id="rso"]/div[3]/div/div[1]
#//*[@id="rso"]/div[3]/div/div[2]<>sjshsgs<>

#o = drv.find_element_by_xpath("//*[@id='rso']/div[3]/div/div[1]")
#txt = o.get_attribute('innerHTML')
o = drv.find_element_by_class_name("iUh30")
txt = o.get_attribute('innerHTML')

print(txt)


o = drv.find_elements_by_class_name("iUh30")
for e in o:
    txt = e.get_attribute('innerHTML')
    print(txt)
    














