import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import csv
from random import randint
from time import sleep



def send_mail(fromaddr, frompasswd, toaddr, msg_subject, msg_body, file_path):
    try:
        msg = MIMEMultipart()
        print("[+] Message Object Created")
    except:
        print("[-] Error in Creating Message Object")
        return

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = msg_subject

    body = msg_body

    msg.attach(MIMEText(body, 'plain'))

    filename = file_path
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    try:
        msg.attach(p)
        print("[+] File Attached")
    except:
        print("[-] Error in Attaching file")
        return

    try:
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        s = smtplib.SMTP('stud.iitp.ac.in', 587)
        print("[+] SMTP Session Created")
    except:
        print("[-] Error in creating SMTP session")
        return

    s.starttls()

    try:
        s.login(fromaddr, frompasswd)
        print("[+] Login Successful")
    except:
        print("[-] Login Failed")

    text = msg.as_string()

    try:
        s.sendmail(fromaddr, toaddr, text)
        print("[+] Mail Sent successfully")
    except:
        print('[-] Mail not sent')

    s.quit()


def isEmail(x):
    if ('@' in x) and ('.' in x):
        return True
    else:
        return False




FROM_ADDR = "piyush_2001me45@iitp.ac.in"
FROM_PASSWD = ""

Subject = "tutorial 6  "
Body ='''
sir please find the attchiment

Thanking You.
 
--
PIC Automation
IIT Patna
'''
from datetime import datetime
file_path="output\\attendance_report_consolidated.xlsx"
start_time = datetime.now()


to='piyushgautam433@gmail.com'



if(len(to)==0):
    print("please enter the email addrsss")
else:
#what a ever is the limit of your sending mails, like gmail has 500.
   send_mail(FROM_ADDR, FROM_PASSWD,to , Subject, Body, file_path)

end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))