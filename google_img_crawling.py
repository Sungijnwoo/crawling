from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from argparse import ArgumentParser
from tqdm import tqdm
import os


img_size = {'all': '74', 'big': '75', 'middle': '76', 'icon': '77', '400': '78', '600': '79', '800': '7a', '1024': '7b', '2mb': '7c', '4mb': '7d', '6mb': '7e',
            '8mb': '7f', '10mb': '7g', '12mb': '7h', '15mb': '7i', '20mb': '7j', '40mb': '7k', '70mb': '7l'}
img_format = {'all': '6r', 'jpg': '6s', 'gif': '6t', 'png': '6u', 'bmp': '6v', 'svg': '6w', 'webp': '6x', 'ico': '6y', 'raw': '6z'}
img_license = {'all': '6n', 'creative': '6o', 'commercial': '6p'}

def parse_args():
    parser = ArgumentParser()

    parser.add_argument('--query', type=str, default=None, help="select word that you want to search")
    parser.add_argument('--goal_cnt', type=int, default=10, help="choose how many image you get")
    parser.add_argument('--img_format', type=str, default='all', help="select format all|jpg|gif|png|bmp|svg|webp|ico|raw")
    parser.add_argument('--img_size', type=str, default='all', help='choose minimum img size all|big|middle|icon|400|600|800|1024|2mb|4mb|6mb|8mb|10mb|12mb|15mb|20mb|40mb|70mb')
    parser.add_argument('--img_license', type=str, default='all', help="select img license all|creative|commercial")
    parser.add_argument('--save_dir', type=str, default='./imgs', help='choose save dir')
    args = parser.parse_args()
    return args

def main(args):
    driver = webdriver.Chrome(r"D:\crawling\chromedriver.exe")
    driver.get(f'https://www.google.co.kr/advanced_image_search?hl=ko&fg=1&q={args.query}&sa=X&ved=2ahUKEwjZhNuPtZT0AhV-QfUHHTnzBZ4Q7psIegQIABAH')
    # driver.get('https://ko.depositphotos.com/stock-photos/3d-cad-%EA%B1%B4%EC%B6%95.html?offset=60')

    serach_size_box = driver.find_element_by_xpath('//*[@id="imgsz_button"]')
    serach_size_box.click()
    select_size = driver.find_element_by_xpath(f'//*[@id=":{img_size[args.img_size]}"]')
    select_size.click()

    search_color_box = driver.find_element_by_xpath('//*[@id="gmcr_imgc2"]/div/span[1]')
    search_color_box.click()

    search_format_box = driver.find_element_by_xpath('//*[@id="as_filetype_button"]')
    search_format_box.click()
    select_format = driver.find_element_by_xpath(f'//*[@id=":{img_format[args.img_format]}"]')
    select_format.click()

    search_autority_box = driver.find_element_by_xpath('//*[@id="as_rights_button"]')
    search_autority_box.click()
    search_autority = driver.find_element_by_xpath(f'//*[@id=":{img_license[args.img_license]}"]')
    search_autority.click()

    search_button = driver.find_element_by_xpath('//*[@id="s1zaZb"]/div[5]/div[10]/div[2]/input[2]')
    search_button.click()


    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    save_cnt = 0
    pbar = tqdm(total=args.goal_cnt)
    os.makedirs(args.save_dir, exist_ok=True)
    for img in images:
        try:
            img.click()
            time.sleep(1)
            img_url = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
            urllib.request.urlretrieve(img_url, f"{args.save_dir}/test{save_cnt:04}" + ".jpg")
            save_cnt += 1
            pbar.update(1)
        except:
            pass
        if save_cnt == args.goal_cnt:
            break
    driver.close()

if __name__ == "__main__":
    args = parse_args()
    main(args)

