import time
import math
import calendar
import email
import warnings as warn
import webbrowser as web
import random
import zipfile as zip
import os
import smtplib
import imaplib
import email as em
from email.header import decode_header
# That's all we need for the modules, as we have pretty much everything we need.

# Some custom commands
def calculate(operation, num1, num2):
    if operation == 'add' or operation == '+':
        opSys = "+"
        return num1 + num2
    elif operation == 'subtract' or operation == '-':
        opSys = "-"
        return num1 - num2
    elif operation == 'multiply' or operation == '*':
        opSys = "*"
        return num1 * num2
    elif operation == 'divide' or operation == '/':
        opSys = "/"
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."
        
def send_email(sender, password, recipient, subject, body):
    msg = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg)

def receive_emails(email_user, email_password):
    mails = []
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(email_user, email_password)
    imap.select('inbox')
    status, messages = imap.search(None, 'ALL')
    mail_ids = messages[0].split()
    latest_emails = mail_ids[-10:]  # Get the last 10 emails
    for i in latest_emails:
        status, msg_data = imap.fetch(i, '(RFC822)')
        msg = em.message_from_bytes(msg_data[0][1])
        mails.append(msg)
    imap.logout()
    return mails


# Run the system
cmds = "time, calc, email, web, dice, timer, cmds"
print("Commands: " + cmds)
while True:
  command = str(input("KITSUNE-CMD: "))
  if command == "time":
    now = time.time()
    currenttime = time.strftime("%Y-%m-%d %H:%M:%S")
    print("The current time is: " + currenttime)
  elif command == "calc":
    operation = input("Enter a math operation (add, subtract, multiply, divide, +, -, *, /): ").strip().lower()
    if operation == 'add' or operation == '+':
        opSys = "+"
    elif operation == 'subtract' or operation == '-':
        opSys = "-"
    elif operation == 'multiply' or operation == '*':
        opSys = "*"
    elif operation == 'divide' or operation == '/':
        opSys = "/"
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = calculate(operation, num1, num2)
    print(f"{num1} " + opSys + f" {num2} = {result}")
  elif command == "email":
        print("Choose an option:")
        print("1: Send Email")
        print("2: Receive Emails")
        print("3: Register (Open Gmail Sign In)")
        option = input("Select an option (1, 2, or 3): ").strip()
        
        if option == '1':
            sender = input("Enter your email: ")
            password = input("Enter your password: ")
            recipient = input("Enter recipient's email: ")
            subject = input("Enter subject: ")
            body = input("Enter email body: ")
            send_email(sender, password, recipient, subject, body)
            print("Email sent!")
        
        elif option == '2':
            email_user = input("Enter your email: ")
            email_password = input("Enter your password: ")
            emails = receive_emails(email_user, email_password)
            for i, email in enumerate(emails):
                subject, encoding = decode_header(email.get("Subject"))[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
                print(f"Email {i + 1}: Subject: {subject}")
        
        elif option == '3':
            web.open("https://accounts.google.com/ServiceLogin?service=gmail")
        else:
            print("Invalid option. Please select 1, 2, or 3.")
    elif command == "web":
        site = int(input("Please pick from URL (1) or Google Search (2)."))
        if site == 1:
            siteurl = input("Please type the URL you would like to open, after https://")
            web.open(str(f"https://{siteurl}"))
        elif site == 2:
            siteurl = input("Please type the term you would like to search: ")
            web.open(str(f"https://www.google.com/search?q={siteurl}"))
        else:
            print("Invalid request.")
    elif command == "dice":
        dicesize = int(input("What size of dice do you want? d"))
        diceoutput = random.randint(1, dicesize)
        print("Your d" + str(dicesize) + " rolled a " + str(diceoutput) + ".")
    elif command == "timer":
        timer = int(input("How long do you want to set the timer for? (In seconds) "))
        timerint = 0
        while timerint != timer:
            timeleft = timer - timerint
            print("Time Remaining: " + str(timeleft))
            time.sleep(1)
            timerint = timerint + 1
        print("Your " + str(timer) + " second timer is up.")
    elif command == "cmds":
        print("Commands: " + cmds)
