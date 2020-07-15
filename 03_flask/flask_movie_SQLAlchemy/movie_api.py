import urllib.request 
import json, datetime, time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 일별 박스오피스
def cineBoxInfo():
    #오늘 날짜를 가져와서 사용할 형식으로 만든다.
    movieDate=time.strftime('%Y%m%d', time.localtime(time.time()))
    
    cine=[]
    for i in range(0,30):
        #자료는 매일 갱신되며 갱신 시간이전에 요청시 내용이 비어 있음.
        #반복 함수 마지막에 날짜를 줄이는 함수를 사용한다.
        #str -> date
        datetime_obj = datetime.datetime.strptime(movieDate,"%Y%m%d").date()

        # 1일 혹은 1주일씩 시간을 줄여간다.
        datetime_obj_tmp = datetime_obj - datetime.timedelta(days=1)  #weeks=1
        
        #date -> str
        movieDate = datetime_obj_tmp.strftime("%Y%m%d")
        print(movieDate, end=" ")
                
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=66e652e1d2656b42f10d93c91e0295e4&targetDt={movieDate}"
        response =urllib.request.urlopen(url)
        #print(response)
        
        rescode = response.getcode()
        if(rescode == 200):
            responseData = response.read()

        result = json.loads(responseData)
        #print(result)
        pre_result = result["boxOfficeResult"]["dailyBoxOfficeList"]
        #print(pre_result)     
        
        for i in range(0,len(pre_result)):
            pre_result[i]['targetDt']=movieDate
            cine.append(pre_result[i])
      
    print()
    #list->dataframe
    dataframe=pd.DataFrame(cine)
    print(dataframe.columns)
    dataframe.to_csv("cinebox.csv", index = False)
    return dataframe

