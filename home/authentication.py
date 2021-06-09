import smtplib
from email.message import EmailMessage
import threading
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


SENDER = "com.sarfarajansari@gmail.com"
PASSWORD = "canttellyou"


def mailwithhtml(html):
    

    # Pass 'alternative' to the MIMEMultipart constructor.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "you have received a message"
    msg['From'] = SENDER
    msg['To'] = "sakiri4444@gmail.com"


    msg.attach(MIMEText(html, 'html', 'utf-8'))

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(SENDER, PASSWORD)
    server.send_message(msg)
    server.quit()

def SendMailWithHtml(html):
    arglist = [html]
    sendmails = threading.Thread(target=mailwithhtml, name="sending mail", args=arglist)
    sendmails.start()


