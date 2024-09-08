import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

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
            logging.info("Succesfully logged in to Outlook server.")
            if self.message:
                server.sendmail(from_addr=self.message['From'],
                                to_addrs=self.message['To'],
                                msg=self.message.as_string())
                logging.info("Mail sent successfully")

        except Exception as error:
            logging.error(f"There was an error sending mail: {error}")

        finally:
            server.quit()
