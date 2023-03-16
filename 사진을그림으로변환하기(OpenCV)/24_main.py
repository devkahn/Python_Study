#24 사람을 그림으로 변환하기(OpenCV)

## pip install opencv-python - OpenCV는 이미지처리 영상처리 분야에서 유명한 라이브러리


### 여행사진을 그림으로 변환하는 코드 만들기

import numpy as np
import cv2

ff = np.fromfile(r'pjt24_사진을그림으로변환하기(OpenCV)\water-3354062_1920.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)

cv2.imshow('cartoon view', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


### 실시간으로 사진이 변하는 코드 만들기

def onChange(pos):
    pass

cv2.namedWindow('Trackbar Windows')
cv2.createTrackbar('sigma_s', 'Trackbar Windows', 0, 200, onChange)
cv2.createTrackbar('sigma_r', 'Trackbar Windows', 0 ,100, onChange)

cv2.setTrackbarPos('sigma_s', 'Trackbar Windows', 100)
cv2.setTrackbarPos('sigma_r', 'Trackbar Windows', 10)

while True:
    if cv2.waitKey(100) == ord('q'):
        break
    
    sigma_s_value = cv2.getTrackbarPos('sigma_s', 'Trackbar Windows')
    sigma_r_value = cv2.getTrackbarPos('sigma_r', 'Trackbar Windows') /100.0
    
    print('sigma_s_value : ' , sigma_s_value)
    print('sigma_r_value : ' , sigma_r_value)
    
    cartoon_img  = cv2.stylization(img, sigma_s= sigma_s_value, sigma_r=sigma_r_value)
    
    cv2.imshow('Trackbar Windows', cartoon_img)
    
    
cv2.destroyAllWindows()