#26 로또번호 시각화하기

## pip install openpyxl - 엑셀을 사용하기 위한 라이브러리


### 판다스로 값 일고 그래프로 그리는 코드 만들기
import pandas as pd

file_paht = r'pjt26_로또번호시각화하기\res\lottery.xlsx'
df_from_excel = pd.read_excel(file_paht, engine='openpyxl')

df_from_excel = df_from_excel.drop(index=[0,1]) # 0,1번 줄을 삭제
df_from_excel.columns = [
    '년도', '회차', '추첨일', '1등당첨자수', '1등당첨금액', '2등당첨자수', '2등당첨금액', '3등당첨자수', '3등당첨금액', '4등당첨자수', '4등당첨금액', '5등당첨자수', '5등당첨금액'
    , '당첨번호1', '당첨번호2', '당첨번호3', '당첨번호4', '당첨번호5', '당첨번호6', '보너스번호'
]

# print(df_from_excel.head())
# print(df_from_excel['회차'].values)
# print(df_from_excel['1등당첨금액'].values)



### 회차별 당첨 금액을 그리는 코드
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

df_from_excel['1등당첨금액'] = df_from_excel['1등당첨금액'].str.replace(pat=r'[ ㄱ - |가-힣,]+', repl=r'', regex=True)
df_from_excel['2등당첨금액'] = df_from_excel['2등당첨금액'].str.replace(pat=r'[ ㄱ -|가-힣,]+', repl=r'', regex=True)
df_from_excel['3등당첨금액'] = df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ -|가-힣,]+', repl=r'', regex=True)
df_from_excel['4등당첨금액'] = df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ -|가-힣,]+', repl=r'', regex=True)
df_from_excel['5등당첨금액'] = df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ -|가-힣,]+', repl=r'', regex=True)


df_from_excel['1등당첨금액'] = pd.to_numeric(df_from_excel["1등당첨금액"])
df_from_excel['2등당첨금액'] = pd.to_numeric(df_from_excel["2등당첨금액"])
df_from_excel['3등당첨금액'] = pd.to_numeric(df_from_excel["3등당첨금액"])
df_from_excel['4등당첨금액'] = pd.to_numeric(df_from_excel["4등당첨금액"])
df_from_excel['5등당첨금액'] = pd.to_numeric(df_from_excel["5등당첨금액"])


print(df_from_excel[['1등당첨금액', '2등당첨금액', '3등당첨금액', '4등당첨금액', '5등당첨금액']])

font_path = "c:/windows/fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x= df_from_excel['회차'].iloc[:100].values
price = df_from_excel['1등당첨금액'].iloc[:100].values/100000000

plt.figure(figsize=(10,6))
plt.xlabel('회차')
plt.ylabel('당첨금액(단위:억원)')

plt.bar(x, price, width=0.4)

plt.show()



### 당첨번호의 빈도수를 출력하는 코드 만들기

from collections import Counter

num_list = list(df_from_excel['당첨번호1'].astype(int))
num_list += list(df_from_excel['당첨번호2'].astype(int))
num_list += list(df_from_excel['당첨번호3'].astype(int))
num_list += list(df_from_excel['당첨번호4'].astype(int))
num_list += list(df_from_excel['당첨번호5'].astype(int))
num_list += list(df_from_excel['당첨번호6'].astype(int))

count = Counter(num_list)
most_num = count.most_common(45) #가장 많이 나온 숫자 45개를 찾습니다.

print(most_num)