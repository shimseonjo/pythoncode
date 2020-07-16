import urllib.request,time
from bs4 import BeautifulSoup

#영화제목 가져오기
url='http://www.cgv.co.kr/movies/?ft=0'
response = urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')
#print(soup)
results=soup.select('strong.title')
#print(results)
for result in results:
    print(result.text)
        
