from selenium import webdriver
import math


def calc(i):
    return str(math.log(abs(12*math.sin(int(i)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

x = int(browser.find_element_by_id("input_value").text)

browser.find_element_by_id("answer").send_keys(calc(x))
checkbox = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()
radiobutton = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
