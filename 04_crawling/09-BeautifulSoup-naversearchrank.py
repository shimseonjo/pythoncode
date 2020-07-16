# import urllib.request
# from bs4 import BeautifulSoup

# url = "https://www.naver.com/"
# req = urllib.request.urlopen(url)
# res = req.read()

# soup = BeautifulSoup(res,'html.parser')
# keywords = soup.select(".ah_k")
# #keywords = soup.find_all('span',attrs={"class": "ah_k"})
# #get_text() == 데이터에서 문자열만 추출
# #strip() == 데이터의 양옆 공백제거
# #[:20]의 이유? 인기검색어의 중복을 막고 20위까지만 출력하기 위함
# print(keywords)
# keywords = [each_line.get_text().strip() for each_line in keywords[:20]]


from bs4 import  BeautifulSoup
import urllib.request as req

url="https://datalab.naver.com/keyword/realtimeList.naver"
res=req.urlopen(url)
print(res.read())
soup=BeautifulSoup(res,"html.parser")
searCh=soup.select(".item_title")
print(searCh)
n=1
for i in searCh:
    print(n,"위->"+i.string)
    n+=1

    
