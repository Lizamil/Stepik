import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_begin = "https://stepik.org/lesson/236"

# @pytest.mark.parametrize('url_end', ["895/step/1", "896/step/1", "897/step/1", "898/step/1", "898/step/1", "903/step/1",
#                                      "904/step/1", "905/step/1"])
@pytest.mark.parametrize('url_end', ["898/step/1", "899/step/1", "905/step/1", ])
def test_link(browser, url_end):
    link = url_begin + url_end
    browser.get(link)
    answer = math.log(int(time.time()))
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
    button.send_keys(answer)
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint")))
    test = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    print(test)
    assert test == "Correct!", "___Error____!!!"



