#텍스트를 음성으로 변환
## pip install gtts
## pip install playsound


### 텍스트를 음성으로 변환
from gtts import gTTS

text = "안녕하세요. 파이썬과 49개의 작품들 입니다."
tts = gTTS(text = text, lang='ko')
tts.save(r'03_basicProgram\result\hi.mp3')


### 파이썬 코드에서 텍스트를 음성으로 실행
from playsound import playsound

text = "안녕하세요 뿅뿅프로젝트 입니다."
tts = gTTS(text = text, lang='ko')
tts.save(r'03_basicProgram\result\pppjts.mp3')
playsound(r'03_basicProgram\result\pppjts.mp3')


### 파일에서 문자를 읽어 음성으로 출력하는 코드 만들고 실행

file_path = r'03_basicProgram\res\example.txt.txt'
with open(file_path, 'rt', encoding='UTF-8') as f :
    read_file = f.read()
    
tts = gTTS(text = read_file, lang='ko')
tts.save(r'03_basicProgram\result\report.mp3')
playsound(r'03_basicProgram\result\report.mp3')
