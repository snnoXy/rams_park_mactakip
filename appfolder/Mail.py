import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging


class Mail:
    def __init__(self, outlook_user, outlook_psw, host, port=587):
        self.outlookUser = outlook_user
        self.outlookPsw = outlook_psw
        self.host = host
        self.port = port
        self.message = None

    def prepare_mail(self, subject, body, receiver, name, surname):
        mailText = f"Merhaba {name} {surname},iyi günler.{body}"
        self.message = MIMEMultipart()
        self.message['From'] = self.outlookUser
        self.message['To'] = receiver
        self.message['Subject'] = subject
        self.message.attach(MIMEText(mailText, 'plain'))

    def send_mail(self):
        server = smtplib.SMTP(self.host, self.port)
        server.starttls()

        try:
            server.login(user=self.outlookUser, password=self.outlookPsw)
            if self.message: #None dene
                server.sendmail(from_addr=self.message['From'],
                                to_addrs=self.message['To'],
                                msg=self.message.as_string())
                print("Mail sent successfully")

        except Exception as error:
            print(error)

        finally:
            server.quit()
