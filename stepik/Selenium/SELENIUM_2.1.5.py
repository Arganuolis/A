import math
from selenium import webdriver
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(i):
    return str(math.log(abs(12*math.sin(int(i)))))


image = browser.find_element_by_id('treasure')
x = int(image.get_attribute("valuex"))
y = calc(x)
field = browser.find_element_by_id("answer")
field.send_keys(y)
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()
button = browser.find_element_by_css_selector(".btn-default")
button.click()
