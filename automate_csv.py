# -------------------------------------------------------------------------------
# Imports
import csv
from selenium import webdriver
import time

# -------------------------------------------------------------------------------
# Setup

name = 0
age = 1
score = 2

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # -------------------------------------------------------------------------------
    # Web Automation

    for line in csv_reader:
        driver = webdriver.Chrome(executable_path=r"C:/Users/Rezwan/Documents/Python Scripts/chromedriver.exe")
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeJeRsIv9fABeeSFaKW1XFOkNG4TRzVsU0yzlwzAUY38zx_gg/viewform")

        time.sleep(2)
        name_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        name_field.send_keys(line[0])

        age_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        age_field.send_keys(line[1])

        score_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        score_field.send_keys(line[2])

        submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit.click()

# -------------------------------------------------------------------------------
