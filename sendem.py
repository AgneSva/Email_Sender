import smtplib


from email.mime.text import MIMEText
#multipart so that we could attach plain email and html email(or files)
from email.mime.multipart import MIMEMultipart

#login info to gmail 
username=''
password=''

#takes email text,email subject, sender and reciever
def send(text='teeext', subject='this is my email subject',sender='', reciever=None, html=None):
    # "isinstance" to check if it is a given type or no (if reciever is a list)
    #if it is a list-all good; otherwise run an error
    assert isinstance(reciever,list)

    msg=MIMEMultipart('alternative')
    
    msg['From']= sender
    #we need to separate emails with comma-so using .join
    msg['To']= ",".join(reciever)
    msg['Subject']=subject
    

    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)

    #if there is html in the email,send it as well:
    if html != None:
      html_part=MIMEText(html,'html')
      msg.attach(html_part)
      msg_str=msg.as_string()


#log in to smtp server. open it
    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
#configuration
    server.ehlo()
    #for secure connection
    server.starttls()
    server.login(username,password)
    server.sendmail(sender,reciever,msg_str)
    server.quit()



