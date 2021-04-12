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

waitTime = 15 # time before activating
appName = "Helium" #application to bring to front

def isHeliumRunning():
    #Iterate over the all the running process
    pids = []
    for proc in psutil.process_iter():
        print(proc)
        try:
            # Check if process name contains the given name string.
            if appName.lower() in proc.name().lower():
                pids.append(proc.pid) #append to pids list if more than one instance running
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if pids:
        return pids
    else:
        return 0;

pid = isHeliumRunning()
if (pid == 0):
  print(appName + "not running")
  print("Open " + appName + "? Y / N")
  inp = input()[0].lower()
  if(inp == 'y'):
    # opens helium
    inp2 = input("How many instances?")
    print("opening " + appName)
    for i in range(int(inp2)):
        os.system(f"open -n {appName}.app")
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
for i in pid:
    x = NSRunningApplication.runningApplicationWithProcessIdentifier_(i)
    x.hide()
    time.sleep(1)

    x.unhide()
    time.sleep(2)
print("DONE")
