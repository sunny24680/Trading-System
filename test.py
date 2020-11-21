import smtplib

gmail_user = 'santoshworkacct@gmail.com'
gmail_password = 'amazon2998'

sent_from = gmail_user
to = ['santosh.sunny12@gmail.com', 'yelavarthy24680@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, what\'s up?\n\n- I just sent an email using a python script'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')