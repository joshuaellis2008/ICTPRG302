import smtplib
import pathlib
import shutil
from datetime import datetime
 
import sys
import logging
from backupcfg import backupFile
from backupcfg import srcDir
from backupcfg import srcFile
from backupcfg import dstDir
#!/usr/bin/python3

"""
This Python code demonstrates the following features:

* send an email using the elasticemail.com smtp server.

"""

import smtplib

smtp = {"sender": "30025502@students.sunitafe.edu.au",    # elasticemail.com verified sender
        "recipient": "hwin@sunitafe.edu.au", # elasticemail.com verified recipient
        "server": "in-v3.mailjet.com",      # elasticemail.com SMTP server
        "port": 587,                           # elasticemail.com SMTP port
        "user": "4456e721fb560c0d1f41071676e2f5bd",      # elasticemail.com user
        "password": "8be883bdd74175ccaa5e36879042c0cf"}     # elasticemail.com password

# append all error messages to email and send
def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")

# main function

import sys
import logging
logging.basicConfig(filename=backupFile, level = logging.DEBUG)
loggerfile = logging.getLogger()

#copythe file
#!/usr/bin/python3

import sys
import pathlib
import shutil
from datetime import datetime

def copyFileDirectory():
    """
    This Python code demonstrates the following features:
    
    * extracting the path component from a full file specification
    * copying a file
    * copying a directory.
    
    """
    try:
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")  
        
        #srcFile = "/home/ec2-user/environment/ICTPRG302AssDoc/file1.txt"
       # srcDir = "/home/ec2-user/environment/ICTPRG302AssDoc/dir1"
        
        srcLoc = srcFile # change this srcLoc = srcDir to test copying a directory
        srcPath = pathlib.PurePath(srcLoc)
        
       # dstDir = "/home/ec2-user/environment/ICTPRG302AssDoc/backups"
        dstLoc = dstDir + "/" + srcPath.name + "-" + dateTimeStamp
        
        print("Date time stamp is " + dateTimeStamp) 
        print("Source file is " + srcFile)
        print("Source directory is " + srcDir)
        print("Source location is " + srcLoc)
        print("Destination directory is " + dstDir)
        print("Destination location is " + dstLoc)
        
        if pathlib.Path(srcLoc).is_dir():
            shutil.copytree(srcLoc, dstLoc)
        else:
            shutil.copy2(srcLoc, dstLoc)
    except Exception as e:
        sendEmail(e)
        print("ERROR: An error occurred.")

def main():
    """
    This Python code demonstrates the following features:
    
    * accessing command line arguments.
    
    """
    try:
        argCount = len(sys.argv)
        program = sys.argv[0]
        arg1 = sys.argv[1] #getting job number, user provides the job number
        
        print("The program name is " + program + ".")
        print("The number of command line items is " + str(argCount) + ".")
        print("Command line argument 1 is " + arg1 + ".")
        
        if arg1 == 'job1' or arg1 == 'job2' or arg1 == 'job3': #check if job number is correct
            copyFileDirectory() #copy the filesby calling copyfilediretory function
            loggerfile.error("SUCCESS")
            print("copy by the file")
        else: #if job numer is incorect 
            print("logging and sending email") #send email
            sendEmail("job number is incorrect.")
            loggerfile.error("ERROR - FAIL: Job number is incorrect.") #logging error message
             
    except Exception as e: #catch the unexepted error
        sendEmail(f"Exception occurs {e}")#sending the email alert
        loggerfile.error("Execpiton occurs")#logging error
        print("ERROR - FAIL: An error occurred.", e)
        
    
if __name__ == "__main__":
    main()
    
