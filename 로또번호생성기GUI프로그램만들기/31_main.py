#31 로또번호 생성기 GUI 프로그램 만들기



### 랜덤 번호 중 6개의 번호를 출력하는 코드 만들기

# import random

# lotto_num = range(1,46)

# for i in range(5):
#     print(random.sample(lotto_num,6))
    
    

### tkinter를 이요하여 버튼을 누를 때마다 6개의 랜덤 번호를 출력하느 코드 만들기

# import tkinter
# import tkinter.font
# import random


# lotte_num = range(1,46)

# def buttonClick():
#     print(random.sample(lotte_num,6))


# window = tkinter.Tk()
# window.title('lotto')
# window.geometry("400x200+800+300")
# window.resizable(False,False)

# button = tkinter.Button(window, overrelief='solid', text='번호확인', width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
# button.pack()


#window.mainloop()


### 번호를 누르면 번호를 자동 생성하여 GUI에 표시하는 코드 만들기

import tkinter
import tkinter.font
import random


lotto_num = range(1,46)

def buttonClick():
    for i in range(5):
        lottoPick = map(str, random.sample(lotto_num, 6)) #랜덤으로 생성된 번호 6개를 map함수를 사용하여 문자열로 변환
        lottoPick = ','.join(lottoPick)
        lottoPick = str(i+1) +'회:' + lottoPick
        print(lottoPick)
        listbox.insert(i, lottoPick)
    listbox.pack()
    
    
window = tkinter.Tk()
window.title('lotto')
window.geometry('400x200+800+300')
window.resizable(False,False)

button = tkinter.Button(window, overrelief='solid', text='번호확인', width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

font = tkinter.font.Font(size=20)
listbox = tkinter.Listbox(window, selectmode='extended', height=5, font=font)
listbox.insert(0, '1회:')
listbox.insert(1, '2회:')
listbox.insert(2, '3회:')
listbox.insert(3, '4회:')
listbox.insert(4, '5회:')

listbox.pack()

window.mainloop()


