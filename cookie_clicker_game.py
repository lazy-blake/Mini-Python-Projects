import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)
driver_options.add_argument(
    f"--user-data-dir={user_data_dir}",
)

driver = webdriver.Chrome(options=driver_options)
driver.get("https://ozh.github.io/cookieclicker/")

# time.sleep(4)
# language = driver.find_element(By.CSS_SELECTOR, value="#promptAnchor #langSelect-EN")
# language.click()

cookie_button = driver.find_element(By.ID, value="bigCookie")

wait_time = 5
timeout = time.time() + wait_time

while True:
    cookie_button.click()

    if time.time() > timeout:
        amount = driver.find_element(By.ID, value="cookies").text.split()[0]
        cookie_amount = int(amount.replace(",", ""))

        all_items = driver.find_elements(By.CSS_SELECTOR, value="#products .product")

        for i in all_items[::-1]:
            if "enabled" in i.get_attribute("class"):
                i.click()
                break

        timeout = time.time() + wait_time
