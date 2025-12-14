import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options




def test_login():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(5)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//button[@name='start']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@name='stop']").is_displayed()
    driver.close()


