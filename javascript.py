from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument('--headless')

options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

driver.get('http://pala.tw/js-example/')  # 輸入範例網址，交給瀏覽器
pageSource = driver.page_source  # 取得網頁原始碼
print(pageSource)

driver.close()  # 關閉瀏覽器