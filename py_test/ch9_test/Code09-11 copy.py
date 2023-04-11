import bs4
import urllib.request

nateUrl = "http://hanbit.co.kr/"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('ul', {'class':'top_brand'})

print('## 한빛 출판 네트워크의 메뉴 목록 ##')
li_list = tag.findAll('li')
for li in li_list :
    print(li.text, end='  ' )