import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
 
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '' # your name
email['to'] = '' # email you sending to
email['subject']= '' # your subject here

email.set_content(html.substitute({'name':'anyname'}), 'html')

with smtplib.SMTP(host ="smpt.gmail.com",port = 587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login('','') # (your extra email, the password of the email) 
    smpt.send_message(email)
    print('all done!')