import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
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


# def send_mail(sender, receiver, subject):
#     message = MIMEText(
#         "Anomaly detected in your system, user login failed! and z-score > 5, please find the error and fix it ASAP!"
#     )
#     password = "auex mhqe squb szvs"
#     message["subject"] = subject
#     message["From"] = sender
#     message["To"] = receiver

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender, password)
#     server.sendmail(sender, receiver, message.as_string())
#     server.quit()


# send_mail(
#     "rohanbelsare113@gmail.com",
#     "rohanbelsare113@gmail.com",
#     "WARNING: ANOMALY DETECTED!",
# )

#
# when anomaly is detected and z-score is greater than 4 and less than -3
# @router("/webhook/anomaly/detected/alert")
# def anomaly_detected():
#  z-score
#  if (z-score>=4 && z-score<=-3):
#      send_mail()
#      z-score=[0.25,0.36,1.25,3.56,5.45]

EMAIL="rohanbelsare113@gmail.com"
PASSWORD="auex mhqe squb szvs"
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=465

def send_mail(to_mail:str,anomaly:dict):
    subject="Log anomaly detected"
    body=f"""
        Anomaly detected in system logs
        time window: {anomaly['timestamp']}
        Error count: {anomaly['error_count']}
        Z score: {anomaly['z_score']}
        Please review log data.

        Regards,
        Rohan Belsare.
"""
    msg=EmailMessage()
    msg["subject"]=subject
    msg["from"]=EMAIL
    msg["to"]=to_mail
    msg.set_content(body)

    with smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) as server:
        server.login(EMAIL,PASSWORD)
        server.send_message(msg) 