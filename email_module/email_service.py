import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText 
from email import encoders



class EmailService:
    def __init__ (self,subject,body,sender,recipient,password,smtp_server,port):
        load_dotenv()
        self.subject="Facture mensuelle"
        self.body=body
        self.sender=os.getenv("EMAIL_SENDER")
        self.recipient=os.getenv("EMAIL_RECIPIENT")
        self.password=os.getenv("EMAIL_PASSWORD")
        self.smtp_server=os.getenv("SMTP_SERVER")
        self.port=os.getenv("SMTP_PORT")


    def send_email(self):
        msg=MIMEMultipart()
        msg['Subject']=self.subject
        msg['From']=self.sender
        msg['To']=self.recipient


        msg.attach(MIMEText(self.body,'html'))
        
        print(f"SMTP Server: {self.smtp_server}, Port: {self.port}")
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'facture.json'))

        try:
            with open(file_path,"rb") as attachment:
                part=MIMEBase("application","octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachement; filename={file_path}"
            )
            msg.attach(part)
            print("Attachment added")

            with smtplib.SMTP(self.smtp_server,self.port) as smtp_server:
                #smtp_server.set_debuglevel(1)
                smtp_server.starttls()
                smtp_server.login(self.sender,self.password)
                smtp_server.sendmail(self.sender,self.recipient,msg.as_string())
            print("Email sent successfully")
        except Exception as e:
            print(f"Error: {e}")
            print("Email not sent")


