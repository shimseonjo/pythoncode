'''
show databases;
use test;

테이블 생성하기
create table pages(
id int not null auto_increment primary key,
title varchar(200),
content text,
created timestamp default current_timestamp);
'''
import re,datetime,random,pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup

connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1324',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()

def store(title,content):
    # 따옴표 처리
    title=title.replace("'","''")
    title=title.replace('"','\"')
    content=content.replace("'","''")
    content=content.replace('"','\"')

    sql='insert into pages(title,content) values(%s,%s)'
    cursor.execute(sql,(title,content))
    connection.commit()


def getLinks(url):
    html=urlopen('http://en.wikipedia.org'+url)
    obj=BeautifulSoup(html,'html.parser')
    # h1 태그의 내용
    title=obj.find('h1').get_text()
    # id가 mw-content-text인 div 태그 내부의 p태그의 텍스트
    content=obj.find('div',{'id':'mw-content-text'}).find('p').get_text()
    # 테이블에 저장
    store(title,content)
    # 링크를 리턴함(정규표현식 사용, ^시작, $끝, * 0회 이상 반복)
    return obj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))

# 함수 호출
links=getLinks("/wiki/kevin_Bacon")

try:
    count=0
    while len(links)>0:
        #url 리스트 중에서 랜덤으로 url 선택
        newArticle=links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        #해당 문서에 포함된 새로운 링크를 가져옴
        links=getLinks(newArticle)
        count +=1
        if count>=20:
            break

finally:
    cursor.close()
    connection.close()
    print('완료되었습니다.')