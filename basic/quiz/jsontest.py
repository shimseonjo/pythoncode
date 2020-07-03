import json
 
# 테스트용 Python Dictionary
customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

# json.dump 파일로 바로 저장
with open('./basic/quiz/data.json','wt') as f:
    json.dump(customer,f,indent=4)


# # json.loads json 문자를 읽어서 파이썬 객체로 변경
# customer1 = json.loads(jsonString)
# print(customer1)

# # json.load json 파일을 읽어서 파이썬 객체로 변경
with open('./basic/quiz/data.json','rt') as f:
    customer2 = json.load(f)
    print(type(customer2))
    print(customer2)


     
# JSON 인코딩
# jsonString = json.dumps(customer)
 
# 문자열 출력
# print(jsonString)
# print(type(jsonString))   # class str

# json.dumps 파이썬내에서 바로 사용
# jsonString = json.dumps(customer, indent=4)
# print(jsonString)
