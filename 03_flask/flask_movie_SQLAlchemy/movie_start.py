import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def Getdata(code_list,page=None):
    # 영화 코드
    # code_list = code_list    
    # 현재 크롤링 중인 영화가 첫 번째 영화인지 여부
    # chk = False
    # 영화의 개수만큼 반복한다.
    df = pd.DataFrame()
    
    for code in code_list:
        # 1단계 : 해당 영화의 평점 페이지 수 계산
        # 접속한다.
        site1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'.format(code)
        res1 = requests.get(site1)
        if res1.status_code == requests.codes.ok:
            # html코드를 분석한다.
            bs1 = BeautifulSoup(res1.text, 'html.parser')
            score_total = bs1.find(class_='score_total')
            ems = score_total.find_all('em')
            # print(ems[0].text)
            score_total = int(ems[0].text.replace(',', ''))
            # print(score_total)
            # 페이지 수를 계산한다.
            pageCnt = score_total // 10
            # print(pageCnt)
            if score_total % 10 > 0:
                pageCnt += 1
            # 현재 페이지 번호
            if page!=None and pageCnt>=page:
                pageCnt=page
                
            # print(pageCnt)
            now_page = 1

            # 2단계 : 평점 글 정보와 평점을 가져온다.
            while now_page <= pageCnt:
                sleep(0.5)
                
                # 요청 할 페이지의 주소
                site2 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(code, now_page)
                res2 = requests.get(site2)
                if res2.status_code == requests.codes.ok:
                    bs2 = BeautifulSoup(res2.text, 'html.parser')
                    score_result = bs2.find(class_='score_result')
                    lis = score_result.find_all('li')
                    
                    for obj in lis:
                        # 평점
                        star_score = obj.find(class_='star_score')
                        star_em = star_score.find('em')
                        star_score = int(star_em.text)
                        # 평가글
                        score_reple = obj.find(class_='score_reple')
                        reple_p = score_reple.find('span')
                        score_reple = reple_p.text.strip()
                        # print(star_score, score_reple)
                        # 데이터를 누적한다
                        if score_reple=='' or score_reple=='관람객':
                            continue
                        else:
                            df = df.append([[score_reple, star_score]], ignore_index=True)
                    now_page += 1
                    # print('%d / %d' % (now_page, pageCnt))
    df.columns = ['text', 'star']
    return df