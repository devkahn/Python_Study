#25 가상화폐 데이터 획득하여 데이터베이스에 저장

## pip install pyupbit  - 업비트에서 가상화폐 데이터를 조회할 수 있는 라이브러리 (https://github.com/sharebook-kr/pyupbit)
## DB Browser for SQLite 설치 (https://sqlitebrowser.org/dl/)


### 가상화폐 시세 조회 코드 만들기
import pyupbit


print('--- Coin List ---')
coin_lists = pyupbit.get_tickers(fiat = 'KRW')
print(coin_lists)


print('--- Price Now ---')
price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(price_now)


### 비트코인의 분봉 데이터를 데이터베이스에 저장하는 코드 만들기
import sqlite3
import datetime


ticker ='KRW-BTC' # 한화로 비트코인 데이터를 불러온다
interval = 'minute1' # 분봉 데이터를 불러온다
to = datetime.datetime.now()  # '2023-01-25 13:13' # 해당 시간 이전의 데이터를 불러온다
count = 200 # 불러올 갯수
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to = to, count= count)

db_Path = r'pjt25_가상화폐데이터획득하여데이터베이스에저장\result\coin.db'

con = sqlite3.connect(db_Path, isolation_level=None)
price_now.to_sql('BTC', con, if_exists ='append')

con.close


### 데이터 베이스를 읽는 코드 만들기
import pandas as pd


con = sqlite3.connect(db_Path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC' ", con, index_col='index' )

print(readed_df)



### 비트코인 데이터를 읽어 데이터베이스에 저장하는 코드 만들기


def date_range(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    end = end + datetime.timedelta(days=1)
    dates = [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    
    return dates

dates = date_range("2023-01-01", datetime.datetime.now().strftime("%Y-%m-%d"))

print(dates)


for day in reversed(dates):
    myDay = day + ' 00:00'
    print(myDay)
    
    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = myDay
    count = 1440
    price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)
    
    print(price_now)
    
    con = sqlite3.connect(db_Path, isolation_level=None)
    price_now.to_sql('BTC_23JAN', con, if_exists='append')
    
    con.close
    

### 데이터베이스의 중복을 제거하는 코드

con = sqlite3.connect(db_Path, isolation_level=None)

readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC_23JAN'", con, index_col='index')
readed_df.to_sql('BTC_23JAN_NEW', con, if_exists='replace')

print(readed_df)

