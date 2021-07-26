import smtplib
from email.message import EmailMessage

# the email list of the user
email_list = {
    'niti': 'nithikarehan6d@gmail.com',
    'nitika': 'nithikarehan6d@gmail.com',
    'javi': 'javi.irub@gmail.com',
    'javitha': 'javi.irub@gmail.com',
    'chani': 'chanithuyah@gmail.com',
    'chanithu': 'chanithuyah@gmail.com',
    'me': 'jeenath6e@gmail.com',
    'jeenath': 'jeenath6e@gmail.com',
    'appa': 'yapasat123@gmail.com',
    'amma': 'sunethra8023@gmail.com'
}

# the function which sends the email to the account
def sendEmail(emailo, sub, bodytext):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('eranjan1234567890@gmail.com', 'ThisIsJeenathYapa666^^^222@@@')
    
    emailINFO = EmailMessage()
    emailINFO['From'] = 'eranjan1234567890@gmail.com'
    emailINFO['To'] = emailo
    emailINFO['Subject'] = sub
    emailINFO.set_content(bodytext)

    server.send_message(emailINFO)

# asking input from the console to add the nessesary info to send the email
email = input("give the email to send: ")
subject = input("give your subject for the email: ")
body = input("give your body for the email: ")

# cheking if the email input by the user is a account  
try:
    print(email_list[email])
    sendEmail(email_list[email], subject, body)
except:
    input("error: invalid email name")
    exit()
