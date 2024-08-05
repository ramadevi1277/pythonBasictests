import smtplib
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import encoders as encoders
from email import encoders
import ssl
from os.path import split as path_split


SENDER_EMAIL = "chramadevi210@gmail.com"
APP_PASSWORD = "akxnfpvrrlrlupae"

def send_mail_with_excel():
    msg = MIMEMultipart()
    sender = 'chramadevi210@gmail.com'
    recipients = 'rongala.ramadevi@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)

    msg['Subject'] = 'Quarterly Summary'
    msg['From'] = sender
    msg['To'] = recipients
    body = "this is ramadeci ch210"
    msg.attach(MIMEText(body, "plain"))
    filename = r'C:/users/rcheepurupalli/PycharmProjects/pythonBasictests/excel_file.xlsx'
    attachment = open(r'C:/users/rcheepurupalli/PycharmProjects/pythonBasictests/excel_file.xlsx', 'rb')
    xlsx = MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    xlsx.set_payload(attachment.read())

    encoders.encode_base64(xlsx)
    xlsx.add_header('Content-Disposition', f'attachment; filename="{path_split(filename)[-1]}"')
    msg.attach(xlsx)
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.sendmail(sender, recipients, msg.as_string())
    print("Email Sent suceessfully....")
    server.quit()
    attachment.close()

send_mail_with_excel()