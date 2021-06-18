import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'saran kumar'
email['to'] = 'saranpachaitamilan@gmail.com'
email['subject'] = 'you are placed'
email.set_content('you are placed with a salary of 10L per month')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('lazytobusy@gmail.com', 'Saranrithanyaa7')
    smtp.send_message(email)
    print('message sent!')
