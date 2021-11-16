from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from argparse import ArgumentParser
from tqdm import tqdm
import os


driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get(f'https://ko.depositphotos.com/stock-photos/3d-cad-%EA%B1%B4%EC%B6%95.html?sh=0e045aae578733eedc051e2c4449b02413ac0b3d')
cnt = 0

print('crawling start')
while True:
    images = driver.find_elements_by_xpath('//*[@id="root"]/div/main/div[1]/section/section/article/section/div/div[2]/div/div[2]/section[*]/a')

    for img in tqdm(images):
        try:
            img.click()
        except:
            try:
                check_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/button')
                check_btn.click()
                img.click()
            except:
                close_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/i')
                close_btn.click()
                img.click()
        time.sleep(1)

        try:
            img_url = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/img').get_attribute('src')
            close_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/i')
        except:
            img_url = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div/a/img').get_attribute('src')
            close_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[4]/i')

        urllib.request.urlretrieve(img_url, f"./imgs/{cnt:04}.jpg")
        cnt += 1
        close_btn.click()
        time.sleep(0.5)
        height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, 100)")

    try:
        next_btn = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/section/section/article/section/div/div[3]/a')
        next_btn.click()
        time.sleep(2)
    except:
        break
    

