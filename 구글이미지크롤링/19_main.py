#19 구글 이미지 크롤링

## pip install selenium - 웹을 제어하는 유명한 라이브러리
## pip install webdriver-manager - 웹 드라이버에 사용하는 크롬 드라이버 파일을 손쉽게 다운로드


### 크롬 드라이버를 자동으로 설치하는 코드 만들기

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


driver = webdriver.Chrome(ChromeDriverManager().install()) # 크롬드라이버를 시작합니다. 프로그램이 설치되지 않았다면 프로그램을 자동으로 설치합니다.

URL = 'http://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10) # 사이트로 이동할 때까지 최대 10초 동안 기다립니다.



### 구글 상에서 이미지 크롤링하는 코드 만들기

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromeDriver = webdriver.Chrome('chromedriver')
chromeDriver.get(url = URL)

elem = chromeDriver.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

elem.send_keys('양리라')
elem.send_keys(Keys.RETURN) # 엔터키를 입력하여 검색합니다.


import time

elem = chromeDriver.find_element(By.TAG_NAME, 'body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)


links =[]
images = chromeDriver.find_elements(By.CSS_SELECTOR, '#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')

print('이미지 객체 수: ', len(images))

for image in images:
    print(image.get_attribute('src'))
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))
        
print('찾은 이미지 개수' , len(links))


### 크롤링한 이미지 다운로드 받는 코드 만듥

import urllib.request

for k,i in enumerate(links):
    url = i
    fileName = r'pjt19_구글이미지크롤링\reult' +'\\' + str(k) + '.jpg'
    urllib.request.urlretrieve( url, fileName)
    print(i+"번째 사진 다운로드 완료")
    
print('다운로드 완료')