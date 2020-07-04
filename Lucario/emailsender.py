##https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class EmailSender:

    def __init__(self,params):
        self.mail_content = params.get('mail_content')
        self.sender = params.get('sender_address')
        self.receiver = params.get('receiver_address')
        self.password = params.get('password')
        self.subject = params.get('email_subject')

    def email_message(self):
        message = MIMEMultipart("alternative", None, [MIMEText(self.mail_content, 'html')])
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = self.subject
        return message

    def send_email(self):
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login(self.sender,self.password)
        text = self.email_message()
        session.sendmail(self.sender,self.receiver,text.as_string())
        session.quit()