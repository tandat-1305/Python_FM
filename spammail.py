import smtplib
server = smtplib.SMTP('smtp.gmail.com', 535)
server.starttls()
server.login("tandat130502@gmail.com","tandat1607855")
msg = "Spam python test"
for i in range(7):
    if i<7:
        server.sendmail("testpython130502@gmail.com",msg)
        i+=1
server.quit()