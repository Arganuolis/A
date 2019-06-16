from selenium import webdriver
import math


def calc(i):
    return str(math.log(abs(12*math.sin(int(i)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_class_name('btn-primary').click()
browser.switch_to.alert.accept()
browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
browser.find_element_by_class_name("btn-primary").click()
