import smtplib
import os
def mail(email, pssd, mssg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, pssd)
    server.sendmail("email@gmail.com", 'cybercreed010@gmail.com', mssg)
    server.quit()

sender="ghsot"

mainmsg="We want to hire you for this job."
name="Girlss"
email="Gudo@gm.com"
message = f"""From: {name} <{email}>
Subject: New Message On Our Official Website
{mainmsg}
"""
password=os.environ.get('EMAIL_PASS')
mail('wantech010@gmail.com',password,message)
print(message)