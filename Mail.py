import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("our_email","our_pasword")

server.sendmail("from","to","message")

server.quit()