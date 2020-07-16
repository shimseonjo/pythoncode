import urllib.request
import re
from bs4 import BeautifulSoup

url = "https://www.thinkcontest.com/Contest/CateField.html?c=12"
req = urllib.request.urlopen(url)
res = req.read()

soup = BeautifulSoup(res,'html.parser')
#regex: .*(문자의 유형과 상관없이 그것이 반복되면 매칭), ?(그것이 있을 수도 없을 수도 있음)
#.*?(그것은 문자의 반복이지만 있을 수도 없을 수도 있음)
#re.DOTALL == .이 개행문자를 포함한 모든문자를 의미하게함
contests = soup.find_all("div",class_=re.compile("contest-title.*?",re.DOTALL))
keywords = [each_line.a.get_text().strip() for each_line in contests]
print(keywords)
