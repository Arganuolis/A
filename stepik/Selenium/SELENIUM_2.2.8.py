from selenium import webdriver
import os

direc = os.path.abspath(os.path.dirname(__file__)) + '\input.txt'
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector("[placeholder='Введите имя']").send_keys("kek")
browser.find_element_by_css_selector("[placeholder='Введите фамилию']").send_keys("kek")
browser.find_element_by_css_selector("[placeholder='Введите Email']").send_keys("kek")
browser.find_element_by_id("file").send_keys(direc)
browser.find_element_by_class_name("btn-primary").click()
