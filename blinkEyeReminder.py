import time, datetime, threading,subprocess
import getpass
USER_NAME = getpass.getuser()


print(USER_NAME)

# import Pylance
path = r'D:\test'
song = 'alarm_for_iphone_5.mp3'
Path = path + "\\" + song
print('start of program.')

def ring():
    minutes = 60*20
    time.sleep(minutes) 
    
    alarm = subprocess.Popen(['start',Path],shell=True)
    print('Look at the window, stand up bro :)')
    print("Don't sit down!!!")
    wait = 60 * 4
    if alarm.poll == None:
        return True
    time.sleep(wait)
    alarm.wait()
    alarm.poll()
    
    

while True:
    ring()

print('End of the program.')


















"""
# startTime = datetime.datetime(2021,6,12,21,5,0)
# while True:
#     time.sleep(1)
#     print('hello')
"""
"""def takeANap(): # defining the function that we want to implement in  a new thread
    time.sleep(5)
    print('Wake up!')
    print('cats','dogs','frogs',sep=' & ')
"""
"""
# Behind the scenes
import threading
threadObj = threading.Thread(target= print, args=['cats','dogs','frogs'],kwargs = {'sep': ' & '})
threadObj.start()
"""
"""
threadObj = threading.Thread(target= takeANap) # target is not takeANap() ,here because don't want to return value of calling the function, have to give the argument as function itself

threadObj.start()"""