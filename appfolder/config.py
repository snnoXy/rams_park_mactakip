import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
api_key = os.getenv('API_KEY')

today = datetime.today()
day = timedelta(days=1)
tomorrow = today + day

date = str(tomorrow.date())
#date = "2024-08-09"

outlookUser = os.getenv('ADMIN_OUTLOOK')
outlookPsw = os.getenv('ADMIN_OUTLOOK_PASSWORD')
receiverMails = os.getenv('RECEIVER_MAILS').split(',')
receiverNames = os.getenv('RECEIVER_NAMES').split(',')
receiverSurnames = os.getenv('RECEIVER_SURNAMES').split(',')
excelFilePath = os.getenv('EXCEL_FILE_PATH')

mailList = []

for i in range(0, len(receiverMails)):
    mail = {'name': receiverNames[i],
            'surname': receiverSurnames[i],
            'mail': receiverMails[i]}

    mailList.append(mail)
