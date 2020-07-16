from bs4 import BeautifulSoup

html='''
<html>
<body>
<div id="main-goods" role="page">
  <h1>과일과 야채</h1>
  <ul id="fr-list" class="items art it book">
    <li class="red green" data-lo="ko">사과</li>
    <li class="purple" data-lo="us">포도</li>
    <li class="yellow" data-lo="us">레몬</li>
    <li class="yellow" data-lo="ko">오렌지</li>
  </ul>
  </div>
</body>
</html>
'''

soup = BeautifulSoup(html,'html.parser')
header=soup.select_one('body div h1')
list_items=soup.select('ul.items li')

print(header.string)
print(soup.select_one('ul').attrs)
for li in list_items:
    print(li.string)