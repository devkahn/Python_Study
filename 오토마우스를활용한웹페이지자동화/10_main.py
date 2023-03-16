# 오토마우스를 활용한 웹페이지 자동화

## pip install pyautogui - 마우스와 키서울 날씨보드를 자동으로 제어하기 위한 라이브러리
## pip install pyperclip - 클립보드에 값을 복사하거나 붙여넣기 용도로 사용/ pyautogui는 한글지원이 되지 않아 사용


import pyautogui
import time



### 마우스의 좌표를 출력하는 코드 만들기
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)


### 네이버에서 자동으로 서울 날씨 검색하는 코드 만들기
import pyperclip


pyautogui.moveTo(2404,240,0.2)
pyautogui.click()
time.sleep(0.5)


pyperclip.copy("서울 날씨")
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

pyautogui.write(['enter'])
time.sleep(1)


### 서울 날씨 화면 자동 캡쳐 후 저장하는 코드 만들기

start_x = 2431
start_y = 336
end_x = 3036
end_y = 1942

pyautogui.screenshot(r'04_AutomationProgram\pjt10_오토마우스를활용한웹페이지자동화\reuslt\서울날씨3.png', region={start_x, start_y, end_x-start_x, end_y-start_y})
