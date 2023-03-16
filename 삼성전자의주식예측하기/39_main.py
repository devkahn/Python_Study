#39 삼성전자의 주식 예측하기

## pip install tensorflow==2.3 - 인공지능을 사용하기 위한 구글에서 만든 유명한 라이브러리
## pip install keras==2.4.3 - tensorflow를 쉽게 사용할 수 있게 도와주는 라이브러리로 인공지능을 위한 유명한 라이브러리
## pip install pandas-datareader - 주식데이터를 판다스의 형식으로 가져옵니다.
## pip install yfinance - 야후의 주식정보를 쉽게 가져올 수 있는 라이브러리


import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()



### 삼성전자 주식의 10년간 주식 데이터를 불러오는 코드 만들기

now = datetime.now()

berfore = now -relativedelta(years=10)

now_day = now.strftime("%Y-%m-%d")
before_day = berfore.strftime("%Y-%m-%d")
print(f"end : {now_day}" )
print(f"start : { before_day}")

samsung_stock  = pdr.get_data_yahoo("005930.ks", start=before_day, end=now_day)
print(samsung_stock)

close_prices = samsung_stock['Close'].values
print(close_prices)

windown_size = 30

result_list = []
for i in range(len(close_prices)-(windown_size +1)):
    result_list.append(close_prices[i:i+(windown_size+1)])

normal_data = []
for window in result_list:
    window_list = [((float(p) / float(window[0])) -1 ) for p in window]
    normal_data.append(window_list)
    
    
result_list = np.array(normal_data)
print(result_list.shape[0], result_list.shape[1])

row = int(round(result_list.shape[0]*0.9))
train = result_list[:row, :]

x_train = train[:,:-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1],1))
y_train = train[:,-1]

x_test = result_list[row: ,:-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))
y_test = result_list[row:, -1]

print(x_train.shape, x_test.shape)


### 주식 예측 구성 코드 만들기
model = Sequential()
model.add(LSTM(windown_size, return_sequences=True, input_shape =(windown_size,1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(1, activation='linear'))
model.compile(loss ='mse', optimizer='rmsprop')
model.summary()


model.fit(x_train, y_train,
          validation_data = (x_test, y_test),
          batch_size=10,
          epochs=1000
          )

model.save(r'pjt39_삼성전자의주식예측하기\samsung.h5')

pred = model.predict(x_test)

pred_price =[]
for i in pred:
    pred_price.append((i+1) *window[0])
    

real_price=[]
for i in y_test:
    real_price.append((i+1)*window[0])


fig = plt.figure(facecolor='white', figsize=(70,15))
ax = fig.add_subplot(234)
ax.plot(real_price, label='real_price')
ax.plot(pred_price, label='pred_price')
ax.legend()
plt.show()