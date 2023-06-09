from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

find_item = ['косметика','мебель','123']
link = 'https://www.wildberries.ru/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(2)
search_str = browser.find_element(By.ID, 'searchInput')

for el in find_item:
    search_str.clear()
    search_str.send_keys(el)
    search_str.send_keys(Keys.ENTER)
    time.sleep(2)
    detect = browser.find_element(By.CSS_SELECTOR, ".dropdown-filter__btn.dropdown-filter__btn--burger").text
    assert detect==el, 'the test dropped'
