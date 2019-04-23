#!/usr/bin/python -tt
#
# MITG Results Email Project
# SP Mobility AT&T SSPT Team
# Chris Dukes - dukesc@cisco.com
#
import sys
import json
import smtplib
from json2html import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# convert json data into nested html
def jsonconv(infoFromJson):
    print json2html.convert(json = infoFromJson)

# Create and send email
def mailer(SUBJECT, BODY, TO, FROM):

    # Create message container
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please contact <MITG email> for more information">online</a>!"""
    HTML_BODY = MIMEText(BODY, 'html')
    MESSAGE.attach(HTML_BODY)

    # Send the e-mail
    server = smtplib.SMTP('outbound.cisco.com:25')

    # Credentials (if needed) for sending the mail
    #password = "password"

    server.starttls()
    #server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    jsonexample = f.read()
# Debug print
    print jsonexample
    output = json2html.convert(json = jsonexample)
# Debug print
    print output
    TO = 'dukesc@cisco.com'
    FROM ='dukesc@cisco.com'
    mailer("MITG Issue Results", output, TO, FROM)

if __name__ == '__main__':
    main()