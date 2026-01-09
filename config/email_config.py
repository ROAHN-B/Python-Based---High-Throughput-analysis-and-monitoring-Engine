import smtplib
from email.mime.text import MIMEText

# sender = "rohanbelsare113@gmail.com"
# receiver = "rohanbelsare113@gmail.com"
# password = "auex mhqe squb szvs"

# message = MIMEText("Sending mail using python")

# message["subject"] = "test Email"
# message["From"] = sender
# message["To"] = receiver

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()  # for encryption
# server.login(sender, password)
# server.sendmail(sender, receiver, message.as_string())
# server.quit()


def sending_mail(sender, receiver, subject):
    message = MIMEText("sending mail using python")
    message["subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    password = "auex mhqe squb szvs"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()


sending_mail(
    "rohanbelsare113@gmail.com",
    "rohanbelsare113@gmail.com",
    "sending mail using python",
)
