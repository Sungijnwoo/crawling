## Crawling 사용법

### package
```
pip install -r requirements.txt
```

### chromdriver.exe
- first you have to check chrome version
- go into https://chromedriver.chromium.org/downloads
- download proper version of chromedriver

### news_crawling.py

- to download news in naver
```bash
press_list : choose press where you want to crawling
query : choose query that you want to search
news_num : choose how many news you have
code : python news_crawling.py
```

### google_img_crawling.py

- to download image in google with advanced filter
```bash
python google_img_crawling.py --query [query] --goal_cnt [cnt]
```
 
