import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "chramadevi210@gmail.com"
APP_PASSWORD = "akxnfpvrrlrlupae"

def send_mail_with_excel(recipient_email, subject, content, excel_file):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content(content)
    with open(excel_file, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=excel_file)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #import pdb;pdb.set_trace()
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print("EMAIl Sent succesfilyy.................")
excel_file = 'C:/users/rcheepurupalli/PycharmProjects/pythonBasictests/excel_file.xlsx'

send_mail_with_excel('rongala.ramadevi@gmail.com', "test_mail,", 'hi how are you doing.....', excel_file)