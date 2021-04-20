from Cocoa import *
import objc
import time
import psutil
import sys
import os

waitTime = 15 # time before activating
appName = "Helium" #application to bring to front

def get_helium_pids():
    #Iterate over the all the running process
    pids = []
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if appName.lower() in proc.name().lower():
                pids.append(proc.pid) #append to pids list if more than one instance running
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pids

def bring_to_front(pids):
    for i in pids:
        time.sleep(1)
        x = NSRunningApplication.runningApplicationWithProcessIdentifier_(i)
        x.hide()
        time.sleep(1)

        x.unhide()
        print(f"{i} was unhid!")

pid = get_helium_pids()
pid_length = len(pid)
if (not pid):
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
    pid = get_helium_pids() # assigns new pid
    pid_length = len(pid)
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

bring_to_front(pid)

while True:
    time.sleep(120)
    while len(get_helium_pids()) is not pid_length:
        os.system(f"open -n {appName}.app")
        print(f"opened {appName} again")
        bring_to_front(get_helium_pids())
print("DONE")
