# 영어 문서를 한글로 자동번역
## pip install googletrans==4.0.0-rc1


import googletrans

### 번역 프로그램 코드 만들기

translator = googletrans.Translator()

print()
print('번역 프로그램 코드 만들기')
print()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='auto')
print(f'{str1}==> {result1.text}')

str2 = 'I am sad.'
result2 = translator.translate(str2, dest='ko', src='en')
print(f'{str2} ==> {result2.text}')


lang = googletrans.LANGUAGES
#print(lang)
langCode = googletrans.LANGCODES
#print(langCode)



### 영어 문서를 한글로 번역하는 코드 만들기
from os import linesep

read_file_path = r'04_AutomationProgram\res\entoko.txt'
write_file_path = r'04_AutomationProgram\res\vueKor.txt'

with open(read_file_path, 'r') as f:
    readlines = f.readlines()
    
for line in readlines:
    result = translator.translate(line, dest='ko')
    print(result.text)
    with open(write_file_path, 'a', encoding='utf8') as f:
        f.write(result.text +'\n')
