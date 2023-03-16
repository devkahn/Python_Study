#환율 변환기
## pip install currencyconverter


from currency_converter import CurrencyConverter

### 지원되는 통화목록 출력 코드 만들기
print('지원되는 통화목록 출력 코드 만들기')
print()
cc = CurrencyConverter()
print(cc.currencies)


### 1달러를 워화로 변환한 결과 출력 코드 만들기
print()
print('1달러를 원화로 변환한 결과 출력 코드 만들기')
print()
cc2 = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc2.convert(1,'USD', 'KRW'))



### 실시간 환율 정보 크롤링 코드 만들기
print()
print('실시간 환율 정보 크롤링 코드 만들기')
print()


import requests
from bs4 import BeautifulSoup


def get_exchange_rate(target1, target2):
    headers={
        'User-Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text/html; charset=utf-8'
    }
    
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers = headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'class' : 'text-2xl'})
    if containers != "":
        print(containers)
    else:
        print('Tag를 찾을 수 없습니다.')
    

get_exchange_rate('usd', 'cad')