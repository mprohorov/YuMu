import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('teamyumu@gmail.com', 'Gentech16')
s.sendmail('YuMu', '3477387404@mms.att.net', 'You have been invited to a new event!')
s.quit()
