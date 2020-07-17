from bs4 import BeautifulSoup
from selenium import webdriver
import requests,time

driver = webdriver.Chrome('./crawling/data/chromedriver')
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
time.sleep(20)

source=driver.page_source
st_bs=BeautifulSoup(source,'html.parser')
print(st_bs.select('li.quickResultLstCon'))

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(20)

sido = driver.find_element_by_class_name('sido_arae_box')
li=sido.find_elements_by_tag_name('li')
li[3].click()
time.sleep(20)

sido = driver.find_element_by_class_name('gugun_arae_box')
li=sido.find_elements_by_tag_name('li')
li[2].click()
time.sleep(20)

source=driver.page_source

bs=BeautifulSoup(source,'lxml')
entire=bs.find('ul',class_='quickSearchResultBoxSidoGugun')
li_list=entire.find_all('li')

for li in li_list:
    print(li.find('p').text)