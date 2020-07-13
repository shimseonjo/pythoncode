import re

# p = re.compile('ab*')

# m = p.match('abbbc')
# print(m)

# m1 = p.search('babbbc')
# print(m1)

# m2 = re.search('ab*','bacc')

email = input("email 입력")
p= re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
result = p.match(email)
print(result)


