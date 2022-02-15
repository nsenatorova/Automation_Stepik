from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element_by_tag_name("button")
    button.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    result = browser.find_element_by_id('answer')
    result.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()
finally:

    time.sleep(10)
    browser.quit()
