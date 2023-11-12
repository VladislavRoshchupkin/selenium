from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    link = "https://www.wildberries.ru/catalog/15690818/detail.aspx?size=242396273"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, "//div[@class ='product-page__order-container']//button[@class ='btn-main']/span")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
