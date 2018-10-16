#!/usr/bin/python2
__author__ = 'https://github.com/abd0m0hamed'

from datetime import date,datetime
import mysql.connector
import pprint
import time
import smtplib

def getConfig():
    return {
        'user':'root',
        'password':'',
        'host':'localhost',
        'database':'database_name',
        'raise_on_warnings': True
    }


class smtpSender:
    """ SEMTP Sender Class """
    smtp = False
    lastMessage = 0;
    
    def __init__(self):
        print("SMTP Sender Intialized")

    def connect(self):
        try:
            self.smtp = smtplib.SMTP('mail.domain.com:25')
            self.smtp.login("abdo@domain.com","MyVeryComplexPassword")
            return True
        except smtplib.SMTPException as err:
            print('We have an error',err)
            return False

    def disconnect(self):
        self.smtp.close()

    def sendEmail(self,emailAddress):

        try:
            self.smtp.sendmail('from@domain.com', 'to@domain.com', 'Hello From Python')
        except smtplib.SMTPSenderRefused as err:
            print("We Got an error",err)
            return False

        time.sleep(5)
        print("Message Sent To Email Address: ",emailAddress)

        return 0


def getAccounts():
    conn = mysql.connector.connect(**getConfig())
    cur = conn.cursor()
    try:
        print("Getting User Accounts")
        cur.execute("SELECT id,name,email FROM account_user WHERE id > %s limit 5",(self.lastMessage,))
    except mysql.connector.Error as err:
        print(err.msg)

    #print(pprint.pprint(cur.fetchall()))

    s = smtpSender()
    s.connect()

    lastSentId = 0
    for (id, name, email) in cur:
        self.lastMessage = id
        print("Name: ", unicode(name),", Email: ", unicode(email))
        s.sendEmail(email)

    #print("{}, {} was hired on {:%d %b %Y}".format(lastName, firstName, password))

    s.disconnect()
    cur.close()
    conn.close()

    return 0

def start():
    getAccounts()
    sleepMode()

def sleepMode():
    print("Entering to sleep Mode, We will return after Five Minutes")
    time.sleep(300)
    start()


start()
