import urllib.request,time
from bs4 import BeautifulSoup

#벅스에서 차트 노래제목 가져오기
url='https://music.bugs.co.kr/chart'
response = urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')
#print(soup)
results=soup.select('th p a')
#print(results)
for result in results:
    print(result.text)
        
