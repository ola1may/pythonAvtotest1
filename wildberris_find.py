from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.wildberries.ru/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(2)
search_str = browser.find_element(By.ID, 'searchInput')
el ='косметика'
search_str.clear()
search_str.send_keys(el)
search_str.send_keys(Keys.ENTER)
detect=WebDriverWait (browser, 10).until (
    EC.visibility_of_element_located ((By.CSS_SELECTOR, ".dropdown-filter__btn.dropdown-filter__btn--burger")))
text=detect.text
if text == el:
    print ('ok')
