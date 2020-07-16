import urllib
import requests
from bs4 import BeautifulSoup

params=urllib.parse.urlencode({'page':1})
url='https://movie.naver.com/movie/point/af/list.nhn?&%s' %params
print(url)

#params={'page':1}
#url='https://movie.naver.com/movie/point/af/list.nhn'
#res=requests.get(url,params=params)
#print(res.content.decode('euc-kr'))

response = urllib.request.urlopen(url)
navigator=BeautifulSoup(response,'html.parser')
table=navigator.find('table',class_='list_netizen')
# print(table)

list_records=[]
for i,r in enumerate(table.find_all('tr')):
    for j,c in enumerate(r.find_all('td')):
        if j==0:
            print(c.string)
        elif j==1:
            print(c.find('a').string)
            print(c.get_text().replace('신고',''))
        elif j==2:
            print(c)
            # record.update({'평점':int(c.text.strip())})
        elif j==3:
            print(c)
            # record.update({'영화':str(c.find('a',class_='movie').text.strip())})
            # record.update({'140자 평':str(c.text).split('\n')[2]})
        elif j==4:
            print(c)
            # record.update({'글쓴이':c.find('a',class_='author').text.strip()})
            # record.update({'날짜':str(c.text).split('****')[1]})
    # try:
    #     list_records.append(record)
    # except:
    #     pass

print(list_records)
 