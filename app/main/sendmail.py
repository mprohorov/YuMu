import smtplib



def send(pn1, pn2, pn3):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('teamyumu@gmail.com', 'Gentech16')
    s.sendmail('YuMu', (pn1 + '@vtext.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn1 + '@mms.att.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn1 + '@tmomail.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn1 + '@page.nextel.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@vtext.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@mms.att.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@tmomail.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@page.nextel.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@vtext.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@mms.att.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@tmomail.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@page.nextel.com'), 'You have been invited to a new event!')
    s.quit()
#s.sendmail('YuMu', '3475368922@vtext.com', 'You have been invited to a new event!')

def testsend():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('teamyumu@gmail.com', 'Gentech16')
    s.sendmail('YuMu', '3477387404@mms.att.net', 'Test')
    s.quit()

def sendFromDB(pn1, pn2, pn3):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('teamyumu@gmail.com', 'Gentech16')
    s.sendmail('YuMu', (pn1 + '@vtext.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn1 + '@mms.att.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn1 + '@tmomail.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn1 + '@page.nextel.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@vtext.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@mms.att.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@tmomail.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn2 + '@page.nextel.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@vtext.com'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@mms.att.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@tmomail.net'), 'You have been invited to a new event!')
    s.sendmail('YuMu', (pn3 + '@page.nextel.com'), 'You have been invited to a new event!')
    s.quit()

