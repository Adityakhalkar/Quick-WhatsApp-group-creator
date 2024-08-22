from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

filename=input("Enter the name of your csv file without .csv at end: ")

phone_no_column = input("Enter the name of column containing phone numbers: ")

data = pd.read_csv(f'{filename}.csv', encoding='ISO-8859-1')

group_name = input("Enter the name of group into which members are to be added: ")

driver = webdriver.Chrome('')
driver.get('https://web.whatsapp.com')

input("Press Enter after scanning QR code")
try:
    group_chat = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
except:
    print("Group not found. Please enter the correct group name.")
    driver.quit()
    exit()
group_chat.click()
time.sleep(2)  # Wait for the group chat to open
add_participant = driver.find_element(By.XPATH, '//div[text()="Add members"]')
add_participant.click()
time.sleep(2)

numbers = data[f'{phone_no_column}'].to_list()

for number in numbers:
    # Search for the number
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    time.sleep(1)   
    search_box.send_keys(number)
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)
    for i in range(10):
        search_box.send_keys(Keys.DELETE)
    time.sleep(1)

# After adding all numbers, wait for further instructions, Just click the Green tick yourself.
input("Press Enter after adding all participants")

driver.quit()
