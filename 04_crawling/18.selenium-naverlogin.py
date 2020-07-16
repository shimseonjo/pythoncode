from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
#driver = webdriver.Chrome('./crawling/data/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)

id='i_kebi'
pw='!sora14691469'

#driver.find_element_by_name('id').send_keys(id)
#driver.find_element_by_name('pw').send_keys(pw)

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(3)

#element창 로그인버튼 소스 선택된 상태에서 마우스 오른쪽 버튼 클릭 copy
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() 
time.sleep(5)
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
# time.sleep(1)
/html/body/div[1]/div[3]/div/form/fieldset/input
# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')
point = soup.select_one('.my_npoint strong')
print(point.string)

time.sleep(15)
driver.close()
