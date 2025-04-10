from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

contacts = ["Bob", "Charlie"]

group_name = "My Test Group"

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")
print("Scan the QR code and press Enter here after logging in.")
input()

search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(group_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(2)

group_header = driver.find_element(By.XPATH, '//header')
group_header.click()
time.sleep(2)

add_participant = driver.find_element(By.XPATH, '//div[@title="Add participant"]')
add_participant.click()
time.sleep(2)

for contact in contacts:
    search = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search.clear()
    search.send_keys(contact)
    time.sleep(2)
    try:
        user = driver.find_element(By.XPATH, f'//span[@title="{contact}"]')
        user.click()
        time.sleep(1)
    except:
        print(f"Could not find contact: {contact}")

confirm_btn = driver.find_element(By.XPATH, '//span[@data-icon="checkmark"]')
confirm_btn.click()

print("Done adding contacts.")
time.sleep(5)
driver.quit()
