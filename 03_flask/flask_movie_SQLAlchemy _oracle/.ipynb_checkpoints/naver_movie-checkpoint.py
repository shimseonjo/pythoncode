import urllib
from bs4 import BeautifulSoup
import pandas as pd

def naverMovie():
    url='https://movie.naver.com/movie/running/current.nhn'

    response = urllib.request.urlopen(url)
    navigator=BeautifulSoup(response,'html.parser')
    table = navigator.select('ul.lst_detail_t1 li')
    movielist=[]
    # print(type(table))
    # print(table)

    for tt in table:
        thumb=tt.select('div.thumb img')[0]['src']
        # print(thumb)
        title=tt.select('.tit a')[0].string
        # print(title)
        code=int(tt.select('.tit a')[0]['href'].split('=')[1])
        # print(code)

        try:
            time=int(tt.select('.info_txt1 dd')[0].text.split('|')[1].strip()[:-1])
        except:
            time=int(tt.select('.info_txt1 dd')[0].text.split('|')[0].strip()[:-1])
        # print(time)

        try:
            sdate=tt.select('.info_txt1 dd')[0].text.split('|')[2].strip().split()[0]
        except:
            sdate=tt.select('.info_txt1 dd')[0].text.split('|')[1].strip().split()[0]
        # print(sdate)

        grade=tt.select('dt.tit span')[0].text
        # print(grade)

        url='https://movie.naver.com/movie/bi/mi/basic.nhn?code={}'.format(code)
        response = urllib.request.urlopen(url)
        navigator=BeautifulSoup(response,'html.parser')

        try:
            audience = int(navigator.select('div.step9_cont p.count')[0].text.split('(')[0][:-1].replace(",",""))
        except:
            audience=0
        # print(type((audience)))
        # print(audience)

        try:
            summary=navigator.select('div.story_area h5.h_tx_story')[0].text.strip()
        except:
            summary=''
        # print(type((summary)))
        # print(summary)
        movieinfo={'code':code,'title':title,'time':time,'sdate':sdate,'grade':grade,'audience':audience,'summary':summary,'thumb':thumb}
        movielist.append(movieinfo)

    df = pd.DataFrame(movielist)
    # df.to_csv('moviedata.csv')
    # df =pd.read_csv('moviedata.csv')
    # print(df)
    return df


if __name__ =='__main__':
    print(naverMovie())
