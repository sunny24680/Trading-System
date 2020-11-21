import smtplib

gmail_user = 'santosh.sunny12@gmail.com'
gmail_password = 'Padmaja0821'

sent_from = gmail_user
to = ['santosh.sunny12@gmail.com', 'yellowsun24680@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, what\'s up?\n\n- You'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print('connected to server')
    server.ehlo()
    print('test')
    server.login(gmail_user, gmail_password)
    print('logged in')
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')