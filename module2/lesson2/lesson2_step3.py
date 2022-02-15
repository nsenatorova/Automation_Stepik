import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first = browser.find_element_by_id("num1")
    second = browser.find_element_by_id("num2")
    first, second = int(first.text), int(first.text)

    total = str(int(first) + int(second))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(total)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:

    time.sleep(10)
    browser.quit()