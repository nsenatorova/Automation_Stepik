from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    result = browser.find_element_by_id('answer')
    result.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:

    time.sleep(10)
    browser.quit()
