from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./crawling/data/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)

id='i_kebi'
pw='!sora146969'

# driver.find_element_by_name('id').send_keys(id)
# driver.find_element_by_name('pw').send_keys(pw)
# submit = driver.find_element_by_id('log.login')
# submit.click()


driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(3)

#element창 로그인버튼 소스 선택된 상태에서 마우스 오른쪽 버튼 클릭 copy
driver.find_element_by_xpath('//*[@id="log.login"]').click() 
time.sleep(5)

driver.find_element_by_xpath('//*[@id="new.save"]').click()
time.sleep(5)

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
point = soup.select_one('dl.my_npoint strong')
print(point.string)

time.sleep(15)
driver.close()