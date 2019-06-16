from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

sleep(1)
button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text
