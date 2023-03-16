# 이미지에서 글자 추출하기

## pip install pytesseract - 이미지에서 글자를 추출할 때 사용하느 라이브러리

## https://github.com/ub-mannheim/tesseract/wiki - OCR 프로그램 설치



### 이미지에서 한글 찾아 추출하는 코드 만들기
from PIL import Image
import pytesseract

image_Folder = r'pjt22_이미지에서글자추출하기'
image_path = image_Folder  + '\\한글이미지.png'

pytesseract.pytesseract.tesseract_cmd = r'c:\program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(image_path), lang='Kor')

print(text)



### 사용 가능한 언어 확인하는 코드 만들기

lang = pytesseract.get_languages(config='')
print(lang)

# 한국어 사용
## text = pytesseract.image_to_string(Image.open(image_path), lang='Kor')
# 한국어 + 영어 사용
## text = pytesseract.image_to_string(Image.open(image_path), lang='Kor + eng')


### 변환된 언어를 파일로 저장하는 코드 만들기
with open(image_Folder +'\\한글텍스트.txt', 'w', encoding='utf8') as f :
    f.write(text)