#QR코드 생성기

## pip install qrcode
# 다양한 사례 https://pypi.org/project/qrcode/

## pip install image

### QR 코드 생성기
import qrcode


print('QR 코드 생성기')
qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path ='03_basicProgram\\pjt04_QR코드생성기\\result\\'+qr_data +' .png'
#qr_img.save(save_path)


###여러 개의 QR 코드를 한번에 생성하는 코드 만들고 실행
print('여러 개의 QR 코드를 한번에 생성하는 코드 만들고 실행')

file_path = r'03_basicProgram\res\qr코드 모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()
    
    for line in read_lines:
        save_path ='03_basicProgram\\pjt04_QR코드생성기\\result\\'
        print(line)
        qr_data = line.strip()
        qr_img = qrcode.make(qr_data)
        save_path += (qr_data +' .png')
        print(save_path)
        qr_img.save(save_path)