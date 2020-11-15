import random
import smtplib
import string
import tkinter.messagebox as tkMessageBox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

genUsername = ""
genPassword = ""
receiveMail1 = None
def sendValidation(EmailId):
    receiverMail = EmailId

    letters = string.ascii_letters
    genUsername = ''.join(random.choice(letters) for i in range(8))
    genPassword = ''.join(random.choice(letters) for i in range(10))
    emailMsg = "Your Username is:"+genUsername+" and "+"Your Password is:"+genPassword

    try:
        message = MIMEMultipart()
        message['FROM'] = "WARNING!!!Unauthorised entry has been identified..."
        message['To'] = receiverMail
        message['Subject'] = "System generated Username and Password"
        message.attach(MIMEText(emailMsg))

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login("newidlastid@gmail.com", "Divij@1706")
        smtp.sendmail("newidlastid@gmail.com", receiverMail, message.as_string())
        smtp.quit()
    except:
        tkMessageBox.showinfo('Message', 'Cannot send Username and Password please check Internet Connection!!!')

    #receiveMail1 = '{}********{}'.format(receiverMail[0:2], receiverMail[-10:])
    #print("Mail send to:"+receiveMail1)
    return genUsername, genPassword

if __name__ == "__main__":
    sendValidation("kardiledivij@gmail.com")
