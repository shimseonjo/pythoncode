import urllib.request
from bs4 import BeautifulSoup

url='https://finance.naver.com/marketindex/'
response = urllib.request.urlopen(url)

soup=BeautifulSoup(response,'html.parser')
results=soup.select('span.value')
for result in results:
    print(result.string)

print('원달러환율:',results[0].string)    
