import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    result = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", result)
    result.send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:

    time.sleep(10)

    browser.quit()
