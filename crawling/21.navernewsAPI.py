# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os,json
import sys
import urllib.request
client_id = "zI5JyNsOSrWeGL9LyEsX"
client_secret = "E9MLbyuLEF"
encText = urllib.parse.quote("대구")
for i in range(1,1000,100):
    url = "https://openapi.naver.com/v1/search/blog.json?display=100&start=%s&query=%s" %(i,encText)  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    response_body=''
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    
    result = json.loads(response_body)
    for i in range(0,100):
        print(result['items'][0]['title'])
        print(result['items'][0]['description'])
        print()