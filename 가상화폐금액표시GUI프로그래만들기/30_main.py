#30 가상화폐 금액표시 GUI 프로그램 만들기

## pip install pyupbit  - 업비트에서 가상화폐 데이터를 초회할 수 있는 라이브러리
## pip install pyinstaller - .exe의 실행파일로 만들어 코드 상태에서 실행하지 않고 응용 프로그램으로 실행하는 라이브러리



### tkinter를 사용하여 GUI 코드 만들기
import tkinter

window = tkinter.Tk()
window.title('가상화폐 금액표시')
window.geometry('400x200')
window.resizable(False, False)

label = tkinter.Label(window, text='hello')
label.pack()

#window.mainloop()



### 글자 크기를 키우는 코드 만들기
import tkinter.font

font = tkinter.font.Font(size= 30)
label2 = tkinter.Label(window, text='Hello30', font=font)
label2.pack()

#window.mainloop()


### 1초마다 반복해서 동작하는 코드 만들기

font2 = tkinter.font.Font(size=50)
label3 = tkinter.Label(window, text='', font=font2)
label3.pack()

cnt = 0
def get_coin_1sec():
    global cnt
    now_btc_price = str(cnt)
    cnt = cnt+1
    label3.config(text = now_btc_price)
    window.after(1000, get_coin_1sec)
    

get_coin_1sec()

#window.mainloop()



### 1초마다 반복해서 동작하는 GUI 코드 만들기

import pyupbit
import threading
import time


coin_price = 0
def get_coin_price():
    global coin_price
    while True:
        coin_price = pyupbit.get_current_price("KRW-BTC")
        time.sleep(1.0)
        
t1  = threading.Thread(target=get_coin_price)
t1.daemon = True
t1.start()


window2 = tkinter.Tk()
window2.title("비트코인 실시간 가격")
window2.geometry("400x50")
window2.resizable(False,False)

font30 = tkinter.font.Font(size= 30)
labelUpbit = tkinter.Label(window2, text=" ", font=font30)
labelUpbit.pack()


def get_coin_1sec_Upbit():
    global coin_price
    now_btc_price = str(coin_price)
    labelUpbit.config(text=now_btc_price)
    window2.after(1000, get_coin_1sec_Upbit)
    

get_coin_1sec_Upbit()

window2.mainloop()



### exe실행파일 만들고 응용프로그램으로 실행

# 터니멀에서 pyinstall -w -F 파일이름.py