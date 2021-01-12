import smtplib
from tkinter import *
from email.mime.text import MIMEText
#multipart so that we could attach plain email and html email(or files)
from email.mime.multipart import MIMEMultipart



#---------FUNCTIONS-------
#login info to gmail 
username=''
password=''
#subject=''
#sender=''
#reciever=''
#text=''


#to clear all entries
def clear():
     UsernameEntry.delete(0, END) 
     PassEntry.delete(0, END)
     RecEntry.delete(0, END) 
     SubEntry.delete(0, END)
     TxtEntry.delete(0, END)
     
     
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


#------------GUI--------
#main screen
master= Tk()
master.title('Email Sender')


Label(master,text = "Welcome Back!",font=("Arial",24)).grid(row = 0, column=1,sticky = N)
Label(master,text = "Send some emails!",font=("Arial",18)).grid(row = 1, column=1,sticky = W,padx=5)

# Labels for entries
Label(master,text = "Email",font=("Arial",15)).grid(row = 2, sticky = W,padx=5)
Label(master,text = "Password",font=("Arial",15)).grid(row = 3, sticky = W,padx=5)
Label(master,text = "To",font=("Arial",15)).grid(row = 4, sticky = W,padx=5)
Label(master,text = "Subject",font=("Arial",15)).grid(row = 5, sticky = W,padx=5)
Label(master,text = "Body",font=("Arial",15)).grid(row = 6, sticky = W,padx=5)
#for failed messages/to show errors:
Not= Label(master,text = "",font=("Arial",10)).grid(row = 7, sticky =S,padx=5)


#Entries
UsernameEntry=Entry(master, textvariable=username)
UsernameEntry.grid(row=2,column=1)

PassEntry=Entry(master, textvariable=password)
PassEntry.grid(row=3,column=1)

RecEntry=Entry(master, textvariable=reciever)
RecEntry.grid(row=4,column=1)

SubEntry=Entry(master, textvariable=subject)
SubEntry.grid(row=5,column=1)

TxtEntry=Entry(master, textvariable=text)
TxtEntry.grid(row=6,column=1)

#Button 
Button(master,text="SEND",command=send).grid(row=7,column=0,sticky=W, pady=5,padx=15)
Button(master,text="CLEAR",command=clear).grid(row=7,column=1,sticky=W, pady=5,padx=5)

master.mainloop()
