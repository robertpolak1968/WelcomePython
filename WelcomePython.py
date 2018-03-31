import getpass
import datetime
import os
print ("Welcome",getpass.getuser()+",")
now = datetime.datetime.now()
print ("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
cwd = os.getcwd()
print ("Current diretory : ", cwd)
