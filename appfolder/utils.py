from Match import Match
from Mail import Mail
from config import date, outlookPsw, outlookUser,mailList


def get_match_response():
    match = Match(date)
    match.get_match_info()
    match.findSet_data()

    return match

def prepareAndSend_mail(mailList, subject, body):

    mailObject = Mail(outlook_user=outlookUser,
                      outlook_psw=outlookPsw,
                      host='smtp-mail.outlook.com',
                      port=587)

    for mailInfo in mailList:
        receiverName = mailInfo['name']
        receiverSurname = mailInfo['surname']
        receiverMail = mailInfo['mail']

        mailObject.prepare_mail(subject,body,receiverMail,receiverName,receiverSurname)
        mailObject.send_mail()

def create_mail(mailList,match):

    subject = "Rams Park Maç Duyurusu"
    if match.matchState == 1 :
        body = f"\nYarin Rams Park stadyumunda saat {match.matchTime}'da maç vardır.\nTakimlar: {match.firstTeam} ve {match.secondTeam}"
        prepareAndSend_mail(mailList,subject,body)

def add_mails_toList(wanted_mails):
    for mail in wanted_mails:
        if mail not in mailList:
            mailList.append(mail)


