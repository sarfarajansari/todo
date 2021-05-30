import smtplib
import threading
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SENDER = "com.theawesomestore@gmail.com"
PASSWORD = "champstar786"
def valid(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if(re.search(regex, email)):
        return True

    else:
        return False

def mailwithhtml(receiver, html,subject):
    

    # Pass 'alternative' to the MIMEMultipart constructor.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = receiver


    msg.attach(MIMEText(html, 'html', 'utf-8'))

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(SENDER, PASSWORD)
    server.send_message(msg)
    server.quit()

def SendMailWithHtml(receiver, html,subject):
    arglist = [receiver,html,subject]
    sendmails = threading.Thread(target=mailwithhtml, name="Downloader", args=arglist)
    sendmails.start()

def deliverymail(receiver,html):
    # Pass 'alternative' to the MIMEMultipart constructor.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'delivered'
    msg['From'] = SENDER
    msg['To'] = receiver


    msg.attach(MIMEText(html, 'html', 'utf-8'))

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(SENDER, PASSWORD)
    # time.sleep(300)
    server.send_message(msg)
    server.quit()

def senddeliverymail(receiver,html):
    arglist = [receiver,html]
    sendmails = threading.Thread(target=deliverymail, name="Downloader", args=arglist)
    sendmails.start()
