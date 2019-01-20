from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import tkinter as tk
#from tkinter.ttk import Treeview

options = Options()

options.add_argument('--headless')

options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

window = tk.Tk()
window.title('機車比價')
window.geometry('700x600')

tk.Label(window, text='機車or廠牌: ').place(x=50, y=30)
#frame = tk.Frame(window)
#frame.place(x=0, y=100, width=1000, height=280)
#scrollBar = tk.Scrollbar(frame)
#scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
#tree = Treeview(frame, columns=('c1', 'c2', 'c3', 'c4', 'c5'), show="headings", yscrollcommand=scrollBar.set)
#tree.column('c1', width=200, anchor='center')
#tree.column('c2', width=70, anchor='center')
#tree.column('c3', width=130, anchor='center')
#tree.column('c4', width=500, anchor='center')
#tree.column('c5', width=100, anchor='center')
#tree.heading('c1', text='品名')
#tree.heading('c2', text='價錢')
#tree.heading('c3', text='標語')
#tree.heading('c4', text='網址')
#tree.heading('c5', text='出處')

#tree.pack(side=tk.LEFT, fill=tk.Y)
#scrollBar.config(command=tree.yview)
#def link_tree(event):
#    input_id = tree.selection()
#    input_item = tree.item(input_id,"text")

    #for opening the link in browser
#    import webbrowser
#    webbrowser.open('{}'.format(input_item))
    #do whatever you want
#tree.bind("<Double-1>", link_tree)

var_book_name = tk.StringVar()
var_book_name.set('搜尋')
entry_book_name = tk.Entry(window, textvariable=var_book_name)
entry_book_name.place(x=160, y=30)


def insert_point(out):
    t.insert('end', out)


def search():
    t.delete('1.0', 'end')
    #tree.delete(*tree.get_children())
    key = var_book_name.get()
    momo_key = key.replace(' ', '%20')
    momo_url = 'https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%s&searchType=1&cateLevel=1&cateCode=4100500000&curPage=1&_isFuzzy=0&showType=chessboardType' % (momo_key)
    driver.get(momo_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    insert_point('Momo:\n')
    #i = 0
    for goods in soup.select('.goodsUrl'):
        #tree.insert('', i, values=(goods.select('.prdName')[0].text, goods.select('b')[0].text, goods.select('.sloganTitle')[0].text, 'https://www.momoshop.com.tw/%s' % (goods['href']), 'Momo'))
        #i+=1
        output = '品名：%s\n標語：%s\n價錢：$%s\n網址：%s\n' % (goods.select('.prdName')[0].text, goods.select('.sloganTitle')[0].text, goods.select('b')[0].text, 'https://www.momoshop.com.tw/%s' % (goods['href']))
        insert_point(output)

    buybike_key = key.replace(' ', '+')
    buybike_url = 'https://www.buybike.com.tw/?s=%s&lang=en' % (buybike_key)
    driver.get(buybike_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    insert_point('\n\nBuybike:\n')
    for goods in soup.select('.fusion-post-wrapper'):
        try:
            string = goods.select('p')[1].text[goods.select('p')[1].text.index('NT$')+4:goods.select('p')[1].text.index('NT$')+10]
        except ValueError:
            continue
        #tree.insert('', i, values=(goods.select('.entry-title')[0].text, string, '', goods.select('a')[0]['href'], 'BuyBike'))
        #i+=1
        output = '品名：%s\n價錢：$%s元\n網址：%s\n' % (goods.select('.entry-title')[0].text, string, goods.select('a')[0]['href'])
        insert_point(output)

btn_search = tk.Button(window, text='Search', command=search)
btn_search.place(x=170, y=60)
btn_quit = tk.Button(window, text='Quit', command=window.destroy)
btn_quit.place(x=270, y=60)
t = tk.Text(window, height=25)
t.place(x=0, y=100, anchor='nw')
window.mainloop()


#print(soup.prettify())
