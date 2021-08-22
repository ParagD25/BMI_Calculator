from email.mime.text import MIMEText
import smtplib

def send_mail(email,height,weight,user_bmi):
    from_email=''
    from_password=''
    to_email=email

    subject='Your BMI'
    message="Hey there! Your BMI calculated is <strong>%s</strong>, according to your height - <strong>%s</strong> and weight - <strong>%s</strong>." %user_bmi %height %weight

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

