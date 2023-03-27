from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

find_item = ['косметика','мебель','джинсы']
link = 'https://www.wildberries.ru/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
search_str = browser.find_element(By.ID, 'searchInput')

for el in find_item:
    search_str.clear()
    search_str.send_keys(el)
    search_str.send_keys(Keys.ENTER)
    detect = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-filter__btn.dropdown-filter__btn--burger")))
    text = detect.text
    if text==el:
        print('ok')
