import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
#imgurl,subject,rank,author,price= "","","","","",""

null = None
## 함수 선언 부분

# def insertData(subject, author, price, rank, imgurl) :
#     con, cur = None, None
#     data = ""
#     data0, data1, data2, data3, data4, data5 = "", "", "", "", "", ""
#     sql=""

#     con = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='`naverseries_db`', charset='utf8')
#     cur = con.cursor()

#     # data0 = data10
#     data1 = subject; 
#     data2 = author; 
#     data3 = price;
#     data4 = rank;
#     data5 = imgurl;
    
#     try :
        
#         print(null)
#         print(data1)
#         print(data2)
#         print(data3)
#         print(data4)
#         print(data5)
#         sql = "INSERT INTO seriestable (subject, author, price, rank, imgurl)  VALUES('"+ data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','"+ data5 +"')"
#         cur.execute(sql)
        
#     except :
#         print("예외 발생")
#         # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
#     else :
#         print("성공")
#         # messagebox.showinfo('성공', '데이터 입력 성공')
#     con.commit()
#     con.close()
# ##

con, cur = None, None

con = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='`naverseries_db`', charset='utf8')
cur = con.cursor()

naverUrl = "https://series.naver.com/ebook/top100List.series"
while True :
    htmlObject = urllib.request.urlopen(naverUrl,context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    #tag_list = bsObject.findAll('div', {'class': 'lst_thum_wrap'})
    book_list = bsObject.select('div.lst_thum_wrap li')

    print('###### ------------------------- #######')
    num = 1
    
    for book in book_list :

        subject = book.select_one('a strong').text.strip()
        author = book.select_one('a span.writer').text.strip()
        price = book.select_one('p.price2').text.strip()
        rank = book.select_one('em.score_num').text.strip()
        imgurl = book.select_one('img')['src']

        add_book = ("INSERT INTO seriestable "
                    "(subject, author, price, rank, imgurl) "
                    "VALUES (%s, %s, %s, %s, %s)")
        data_book = (subject, author, price, rank, imgurl)
        cur.execute(add_book, data_book)

    con.commit()
    cur.close()
    con.close()
    
    #insertData(subject, author, price, rank, imgurl)
       
    print(subject, author, price, rank)
    print('\t imgLink : '+ imgurl)
    num += 1

    time.sleep(10)