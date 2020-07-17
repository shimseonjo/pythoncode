from bs4 import BeautifulSoup
import requests

starbugs = requests.get('https://www.istarbucks.co.kr/store/store_map.do')
st_bs=BeautifulSoup(starbugs.text,'html.parser')
print(st_bs.select('li.quickResultLstCon'))


