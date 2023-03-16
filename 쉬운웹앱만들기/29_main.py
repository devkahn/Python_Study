#29 쉬운 웹앱만들기

## pip install streamlit - 빠르고 쉽게 웹앱을 만들기 위한 라이브러리
## pip install pyupbit - 업비트에서 가상화폐 데이터를 조회할 수 있는 라이브러리



### streamlit을 이용하여 차트 그리는 코드 만들기
import streamlit as st

# data_list = {1,2,3,4,5,6,7,8,9,10}

# st.write('''
#          샘플데이터
#          ''')


# st.line_chart(data_list)


### 달력에서 날짜를 선택하는 코드 만들기
import datetime

# d = st.date_input(
#     "날짜를 선택하세요",
#     datetime.date.today()
# )

# st.write('선택한 날짜: ', d)



### 선택한 날짜의 비트코인 시세를 그래프로 출력해주는 웹앱 코드 만들기

import pyupbit

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)

st.write('비트코인 1일 차트')

ticker = 'KRW-BTC'
interval = 'minute60'
to = str(d + datetime.timedelta(days=1))
count= 24
price_now = pyupbit.get_ohlcv(ticker=ticker, interval= interval, to=to, count = count)

st.line_chart(price_now.close)