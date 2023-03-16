#40 사진에서 사람을 인식하여 분류하기

## pip install torch - 페이스북 인공지능 개발팀에서 주로 개발을 담당하여 만든 라이브러리
## pip install torchvision - 파이토치의 이미지 인식을 위해 사용



### 이미지를 찾아 리스트의 형태로 반환하는 코드 만들기

from glob import glob

img_path = r'pjt40_사진에서사람을인식하여분류하기\원본이미지'

img_list = glob(img_path +"\*.jpg")
img_list.extend(glob(img_path+'\*.png'))

print(img_list)



### 파이토치를 이용해서 사진 폴더에서 특정 사진을 찾는 코드 만들기
import torch


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

for img_path in img_list:
    results = model(img_path)
    print(img_path)
    results.save(r'pjt40_사진에서사람을인식하여분류하기\이미지확인용')
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])]
        print(tag)
        
        
### 특정 사진을 찾아 특정 폴더로 이동하는 코드 만들기
import shutil
import os

img_move_path = r'pjt40_사진에서사람을인식하여분류하기\사람만분류'

for img_path in img_list:
    results = model(img_path)
    print(img_path)
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])]
        print(tag)
        if tag == 'person':
            print('move')
            shutil.move(img_path, img_move_path + '\\' + os.path.basename(img_path))
            break