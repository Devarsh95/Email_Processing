import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('info.html').read_text())
email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'Enter Recipients Email Address'
email['subject'] = "Add Subject Here"

email.set_content(html.substitute(name='devarsh shinde'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("Enter your email here", "Enter Password")
    smtp.send_message(email)
    print("Sent Mail")
