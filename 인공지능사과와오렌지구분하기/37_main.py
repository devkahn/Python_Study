#37 인공지능 사과와 오렌지 구분하기

## pip install tensorflow==2.3 - 인공지능을 사용하기 위한 구글에서 만든 유명한 라이브러리
## pip install pillow - 이미지 분석 및 처리를 쉽게 할 수 있는  라이브러리

### 학습용 사진 다운로드 받기

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from glob import glob


model_path = r'pjt37_인공지능사과와오렌지구분하기\converted_keras\keras_model.h5'
labels_path = r'pjt37_인공지능사과와오렌지구분하기\converted_keras\labels.txt'
images_list = glob(r'pjt37_인공지능사과와오렌지구분하기\검증용사진\*.jpg')
images_list.extend(glob(r'pjt37_인공지능사과와오렌지구분하기\검증용사진\*.png'))

model = tensorflow.keras.models.load_model(model_path)
data = np.ndarray(shape=(1,224,224,3), dtype=np.float32)


for img_path in images_list:
    image = Image.open(img_path).convert('RGB')
    image.save(img_path)
    size = (224,224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32)/127.0)-1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    print(prediction)

    with open(labels_path, 'rt', encoding='utf8') as f :
        readlines = f.readlines()
        
    if prediction[0,0]> prediction[0,1] :
        print(img_path, readlines[0])
    else :
        print(img_path, readlines[1])
    
    



    
