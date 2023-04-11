import bs4

webPage = open('HTML/Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

a_list = bsObject.findAll('a')

for aTag in a_list :
    print( aTag['href'] )
