#  geckodriver.exe has to be on the global path for python access to it.
# the path is C:\Users\username\AppData\Local\Programs\Python\Python36\Scripts

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert browser.page_source.find('install')
