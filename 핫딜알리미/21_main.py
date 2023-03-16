#핫딜 알리미

## pip install selenium - 웹을 제어하는 유명한 라이브러리
## pip install webdriver-manager - 크롬 드라이버 파일을 손쉽게 다운로드 할 수 있는 라이브러리
## pip install python-telegram-bot - 텔레그램을 사용하기 위한 라이브러리




###사이트의 특정 게시판에서 원하는 키워드가 검색되면 알림 보내는 코드 만들기

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url = URL)
driver.implicitly_wait(time_to_wait=10)

titles = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
urls = driver.find_elements(By.CSS_SELECTOR, '#revolution_main_table > tbody > tr> td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')

for i in range(len(titles)):
    print('타이틀 : ' + titles[i].text)
    print('URL :' + urls[i].get_attribute('href') )
    
    
print('------ 끝 ------')


### 특정 키워드가 포함되면 텔레그램으로 메시지 전송

import telegram

msg = ''
for i in range(len(titles)):
    if '플립' in titles[i].text :
        msg = titles[i].text + '\n' + urls[i].get_attribute('href')
        print(msg)
        token =''
        id = ''
        bot = telegram.Bot(token)
        bot.sendMessage(chat_id=id, text=msg)
