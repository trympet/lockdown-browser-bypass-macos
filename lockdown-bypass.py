#---------------------------------------------------------  
#
# Copyright (c) Trym Lund Flogard. All rights reserved.  
# This code is licensed under the MIT License (MIT).  
# THIS CODE IS PROVIDED *AS IS* WITHOUT WARRANTY OF  
# ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY  
# IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR  
# PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.  
#  
#---------------------------------------------------------
from Cocoa import *
import objc
import time
import psutil
import sys
import os

waitTime = 10 # time before activating
appName = "Helium" #application to bring to front

def isHeliumRunning():
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if appName.lower() in proc.name().lower():
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return 0;

pid = isHeliumRunning()
if (pid == 0):
  print(appName + "not running")
  print("Open " + appName + "? Y / N")
  inp = input()[0].lower()
  if(inp == 'y'):
    # opens helium
    print("opening " + appName)
    os.system("open -a " + appName)
    time.sleep(0.5)
    pid = isHeliumRunning() # assigns new pid
  else:
    print("okay closing...")
    time.sleep(1)
    exit()
print(appName + " found!")
print("PID:" + str(pid))

print("you have " + str(waitTime) + "seconds")
for i in reversed(range(waitTime)):
  time.sleep(1)
  print(str(i) + "...")
  
# hides and unhides app
x = NSRunningApplication.runningApplicationWithProcessIdentifier_(pid)
x.hide()     
time.sleep(1)

x.unhide()
time.sleep(2)    
print("DONE")
