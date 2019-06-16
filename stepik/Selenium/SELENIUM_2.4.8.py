from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(i):
    return str(math.log(abs(12*math.sin(int(i)))))


b = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
b.get(link)

price = WebDriverWait(b, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '10000'))
b.find_element_by_id("book").click()

b.find_element_by_id("answer").send_keys(calc(b.find_element_by_id("input_value").text))
b.find_element_by_id("solve").click()
