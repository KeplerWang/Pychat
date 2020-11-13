import random
import smtplib
from email.mime.text import MIMEText
from Settings import EmailSendException, settings


def verifyCodeGen():
    li = []
    for i in range(6):
        r = random.randrange(0, 5)
        if r == 1 or r == 4:
            num = random.randrange(0, 9)
            li.append(str(num))
        else:
            temp = random.randrange(65, 91)
            char = chr(temp)
            li.append(char)
    r_code = ''.join(li)
    return r_code


def sendVerifyEmail(email):
    verifyCode = verifyCodeGen()
    subject = 'Python_QQ Verify Code'
    content = """Hello, Python_QQ users!
Your VerifyCode: %s""" % verifyCode
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = settings.msgFrom
    msg['To'] = email
    s = None
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(settings.msgFrom, settings.password)
        s.sendmail(settings.msgFrom, email, msg.as_string())
    except smtplib.SMTPException:
        raise EmailSendException
    finally:
        s.quit()
    return verifyCode

