#23 사진에 얼굴만 찾아 모자이크처리(OpenCV)

## pip install opencv-python - OpenCV는 이미지처리 영상처리 분야에서 유명한 라이브러리입니다.


### OpenCV로 얼굴 사진 찾는 코드 만들기
import numpy as np
import cv2

# 얼굴과 눈을 찾기 위한 OpenCV 알고리즘이 적용된 파일을 불러온다
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

# OpenCV에서 한글경로의 파일을 읽지 모새 numpy로 파일을 읽어옵니다.
ff = np.fromfile(r'pjt23_사진에얼굴만찾아모자이크처리(OpenCV)\buddhists-453393_1920.jpg',np.uint8)
# imdecode를 하여 numpy의 이미지 파일을 OpenCV 이미지로 불러옵니다.
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# 이미지의 크기를 조절, fx,fy의 비율로 조절
img = cv2.resize(img, dsize=(0,0), fx = 1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 이미지에서 얼굴을 찾기 위해 회색조 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 여러 개의 얼굴을 찾습니다. ScaleFactor는 감도, minNeighbor : 최소 이격거리 - 두 값을 조절하여 감도의 조절이 가능
faces = face_cascade.detectMultiScale(gray, 1.07,7)
for (x,y,w,h) in faces:
    # 얼굴을 찾아 파란색으로 네모 표시를 한다.
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # 눈을 찾아 녹색 네모 표시
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255.0), 2)


cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




### 사진 속 얼굴을 모자이크 처리하는 코드 만들기

ff2 = np.fromfile(r'pjt23_사진에얼굴만찾아모자이크처리(OpenCV)\people-1979261_1920.jpg',np.uint8)
img2 = cv2.imdecode(ff2, cv2.IMREAD_UNCHANGED)
img2 = cv2.resize(img2, dsize=(0,0), fx = 1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
faces2 = face_cascade.detectMultiScale(gray2, 1.07,7)

for (x,y,w,h) in faces2:
    face_img = img2[y:y+h, x:x+w]
    # 모자이크 크기 조절
    face_img = cv2.resize(face_img, dsize=(0,0), fx=0.1, fy=0.1)
    face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
    img2[y:y+h, x:x+w] = face_img

cv2.imshow('mosaic Face', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()