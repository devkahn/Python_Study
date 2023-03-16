#압축 푸는 코드 만들고 실행

import itertools
import zipfile

pswd_string ='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

zFile = zipfile.ZipFile(r'03_basicProgram\res\res.zip')

for len in range(1,6):
    to_attamp  = itertools.product(pswd_string, repeat=len)
    for attempt in to_attamp:
        passwd = ' '.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd=passwd.encode())
            print(f'비밀번호는 {passwd} 입니다.')
            break
        except:
            pass