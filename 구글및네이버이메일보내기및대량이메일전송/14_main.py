# 구글 및 네이버 이메일 보내기 및 대량 이메일 전송


### 네이버 메일을 보내는 코드 만들기
import smtplib
from email.mime.text import MIMEText


send_email = "gaebok0331@naver.com"
send_pwd = "!qp02wo93ei8"

recv_email = 'gaebok0331@gmail.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587

text = """
메일 내용을 여기에 적습니다.
여러 줄을 입력해도 됩니다.
"""

msg = MIMEText(text)

msg['Subject'] = '메일 제목은 여기에 넣습니다,.'
msg['From'] = send_email
msg['To']= recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()