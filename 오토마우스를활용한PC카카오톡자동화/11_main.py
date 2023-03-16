# 오토마우스를 활용한 PC카카오톡 자동화

## pip install pyautogui - 마우스와 키보드를 자동으로 제어하기 위해 사용
## pip install pyperclip - 클립보드에 값을 복사하거나 붙여넣기 용도(한글지원)
## pip install schedule - 일정시간마다 함수를 동작시킬 때 사용

import pyautogui



### 사진에서 좌표 추출하는 코드 만들기

picPosition = pyautogui.locateOnScreen(r'04_AutomationProgram\res\카카오톡_내사진1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'04_AutomationProgram\res\카카오톡_내사진2.png')
    print(picPosition)
    
if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'04_AutomationProgram\res\카카오톡_내사진3.png')
    print(picPosition);
    
if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'04_AutomationProgram\res\카카오톡_내사진4.png')
    print(picPosition);