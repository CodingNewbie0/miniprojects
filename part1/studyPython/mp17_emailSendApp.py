# 이메일 보내기 앱
import smtplib # Simple Mail Transfer Protocol 메일전송 프로토콜
from email.mime.text import MIMEText # Multipurpose Interner Mail Extestions

send_email = 'XXXXXXX@naver.com' # 실제 아이디
send_pass = 'XXXXXXXX' # 실제 비밀번호
recv_email = 'XXXXXXX@naver.com' # 실제 아이디
smtp_name = 'smtp.naver.com'
smtp_port = 587 # 포트번호

text = '''안녕하세요'''

msg = MIMEText(text)
msg['Subject'] = '메일 제목입니다.'
msg['From'] = send_email # 보내는 메일
msg['To'] = recv_email # 받는 메일
print(msg.as_string())

mail = smtplib.SMTP(smtp_name, smtp_port) # SMTP 객체생성
mail.starttls() # 전송계층보안 시작
mail.login(send_email, send_pass)
mail.sendmail(send_email, recv_email, msg=msg.as_string())
mail.quit()
print('전송완료~')