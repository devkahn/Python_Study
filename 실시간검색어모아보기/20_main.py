#실시간 검색어 모아보기

## pip install selnium - 웹을 제어하는 유명한 라이브러리
## pip install webdriver-manager - 웹 드라이버에 사용하는 크롬 드라이버 파일을 손쉽게 다운로드 할 수 있는 라이브러리



### 크롬에서 실시간 검색 사이트 확인하기

#네이버 실시간 검색 사이트 - signal.bz/news
#줌(포털에서 제공 ) - zum.com
#네이트(포털에서 제공) - www.nate.com


### 파이썬 코드로 제어할 수 있는 크롬 창 띄우는 코드 만들기

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

googleURL = 'https://www.google.co.kr'
driver.get(url = googleURL)
driver.implicitly_wait(time_to_wait=10)


### 실시간 검색어 원소를 찾아 저장하는 코드 만들기

from selenium.webdriver.common.by import By

signalURL = 'https://signal.bz/news'
driver.get(url=signalURL)
driver.implicitly_wait(time_to_wait=10)

naver_results = driver.find_elements(By.CSS_SELECTOR , '#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div > div > a > span.rank-text')

print('<<<네이버 실시간 검색어>>>')
naver_list = []
for naver_keyword in naver_results:
    print(naver_keyword.text)
    naver_list.append(naver_keyword)


### 검색 포털사이트에서 실시간 검색을 확인하는 코드 만들기
nateURL = 'https://www.nate.com'
driver.get(url=nateURL)
driver.implicitly_wait(time_to_wait=10)

driver.find_element(By.CSS_SELECTOR, '#bizRank > div > ol > li.rank03 > p > a').click()

nate_result = driver.find_elements(By.CSS_SELECTOR, )


