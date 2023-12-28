'''
 Name:           generate_email.py
 Description:    send simple email responces to receiver.
 Author:         PJ McMenamin - 17-NOV-2023
 Modified:     
'''
import ssl
import smtplib
from email.message import EmailMessage

class EmailNotification():
    ''' email_notification() class is used to initiate email notification on application '''

    email_sender = 'l00186132.ATU@gmail.com'
    email_password = 'rprq dpnu cyul nmad'
    email_receiver = 'pjmac01@gmail.com'
    subject = 'Sensor Alert'
    body = """
    Notification Temperature Alert Details:

    """

    def __init__(self):
        ''' __init__() function to assign values to object properties '''
        print("Initializing Email Notification Class")


    def send_email(self, param_1: str, param_2: str):
        ''' send_email() function configures SMTP email & sends notification using gmail client'''

        # CODE REFERENCE: following code snipits was taken from youtube.com
        #  - https://www.youtube.com/watch?v=g_j6ILT-X0k
        msg = EmailMessage()
        msg ['From'] = self.email_sender
        msg ['To'] = self.email_receiver
        msg ['Subject'] = param_1 + " " + self.subject
        msg.set_content(self.body + param_2)

        context = ssl.create_default_context()

        try: 
            # Confirm SSL certificate authentication is valid to enables encrypted connection.
            # Otherwise SSL Error would be reported
            #  - ERROR = SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000) 
            cert = ssl.get_server_certificate(('smtp.gmail.com',465))

            if not cert:
                # Allow SMTP with SSL to run on port 465, encrypted connection
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(self.email_sender, self.email_password)
                    smtp.sendmail(self.email_sender, self.email_receiver, msg.as_string())
                    print('encrypted connection')
                    return 1
            else:
                # Allow SMTP to run on port 587, non encrypted connection
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(self.email_sender, self.email_password, initial_response_ok=True)
                    server.ehlo()
                    server.sendmail(self.email_sender, self.email_receiver, msg.as_string())
                    server.close()
                    print('non encrypted connection - SSL certificate update required')
                    return 1
        except Exception as str_error:
                print(str_error)
                return 0
