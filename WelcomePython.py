import getpass
import datetime
print ("Welcome",getpass.getuser()+",")
now = datetime.datetime.now()
print ("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
