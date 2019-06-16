from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = int(browser.find_element_by_id("num1").text)
num2 = int(browser.find_element_by_id("num2").text)
s = str(num1 + num2)
browser.find_element_by_id("dropdown").click()
browser.find_element_by_css_selector('[value="' + s + '"]').click()
browser.find_element_by_class_name("btn-default").click()
