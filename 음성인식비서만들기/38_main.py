#38 음성인식 비서 만들기

## pip install SpeechRecognition - 음성을 텍스트로 변환해주는 라이브러리
## pip install playsound - 음악파일을 파이썬에서 재생하기 위한 라이브러리
## pip install pyaudio - 오디오 I/O 라이브러리


### 음섬을 녹음하는 코드 만들기
import pyaudio
import wave
from playsound import playsound

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = r'pjt38_음성인식비서만들기\output.wav'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print('음성녹음을 시작합니다.')

frames =[]

for i in range(0, int(Rate / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)


print('음성녹음을 완료하였습니다.')

stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b' '.join(frames))
wf.close()

print("녹음된 파일을 재생합니다.")
playsound(WAVE_OUTPUT_FILENAME)


### 음성을 텍스트로 변환하는 코드 만들기
import speech_recognition as sr

try :
    while True:
        r = sr.Recognizer()
        
        with sr.Microphone() as source :
            print('음성을 입력하세요.')
            audio = r.listen(source)
        
        try:
            print("음성변환 : " + r.recognize_google(audio, language='ko-KR'))
        except sr.UnknownValueError:
            print('오디오를 이해할 수 없습니다.')
        except sr.RequestError as e :
            print(f'에러가 발생하였습니다. 에러원인: {e}')

except KeyboardInterrupt:
    pass


### 특정 키워드에 답변하는 음성인식 비서 코드 만들기

try :
    while True:
        r = sr.Recognizer()
        
        with sr.Microphone() as source :
            print('음성을 입력하세요.')
            audio = r.listen(source)
        try :
            stt = r.recognize_google(audio, language='ko-KR')
            print('음성변환 : '  + stt)
            if "안녕" in stt :
                print('네 안녕하세요.')
            elif '날씨' in stt :
                print('정말 날씨가 좋네요.')
        except sr.UnknownValueError:
            print('외오를 이해할 수 없습니다.')
        except sr.RequestError as e :
            print(f'에러가 발행하였습니다. 에러원인:{e}')
except KeyboardInterrupt:
    pass


    