from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()

options.add_argument('--headless')

options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

key = var_book_name.get().replace(' ', '%20')
   momo_url = 'https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%s&searchType=1&cateLevel=1&cateCode=4100500000&curPage=1&_isFuzzy=0&showType=chessboardType' % (key)
    driver.get(momo_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    insert_point('Momo:\n')
    for goods in soup.select('.goodsUrl'):
        output = '品名：%s\n標語：%s\n價錢：$%s\n網址：%s\n' % (goods.select('.prdName')[0].text, goods.select('.sloganTitle')[0].text, goods.select('b')[0].text, 'https://www.momoshop.com.tw/%s' % (goods['href']))
        insert_point(output)
https://shopping.udn.com/mall/cus/search/Search.do