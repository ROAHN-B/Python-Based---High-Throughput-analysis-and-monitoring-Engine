import smtplib
from email.mime.text import MIMEText

sender = "rohanbelsare113@gmail.com"
receiver = "rohanbelsare113@gmail.com"
password = "auex mhqe squb szvs"

message = MIMEText("Sending mail using python")

message["subject"] = "test Email"
message["From"] = sender
message["To"] = receiver

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  # for encryption
server.login(sender, password)
server.sendmail(sender, receiver, message.as_string())
server.quit()
