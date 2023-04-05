import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "comsphddev@gmail.com"
Reciever_Email = "miswindall@gmail.com"
Password = '1gd2894JJq9x'

newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Dail Data Drop" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email
newMessage.set_content('time & date???') #Defining email body

files = ["plot1.png", "plot2.png"]

for file in files:
    with open(file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password) #Login to SMTP server
    smtp.send_message(newMessage)      #Sending email using send_message method by passing EmailMessage object
