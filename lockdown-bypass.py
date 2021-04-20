from Cocoa import *
import objc
import time
import psutil
import sys
import os

# Change this variable to shorten
# or increase the time before activation 
activation_timer_seconds = 15

# This is the name of the application which
# should remain visible.
app_name = "Helium"

def run():
    pids = get_helium_pids()
    print_and_wait_countdown()
    bring_to_front(pids)

    while True:
        time.sleep(120)
        number_of_instances = len(pids)
        while len(get_helium_pids()) is not number_of_instances:
            print(f"Instance count changed.")
            open_helium()
            print(f"Opened {app_name} again")
            bring_to_front(get_helium_pids())

def get_helium_pids():
    pids = get_pids_for_name(app_name)
    if (not pids):
        answer = input(f"{app_name} not running\nOpen {app_name}? Y / N")
        if(answer[0].lower() == 'y'):
            instance_count = input("How many instances?")
            open_helium(instance_count)
            time.sleep(0.5)
            pids = get_pids_for_name(app_name)
        else:
            print("Okay closing...")
            time.sleep(1)
            exit()
            
    print(f"Found {app_name} with pids {str(pids)}")
    return pids

def get_pids_for_name(name):
    pids = []
    for proc in psutil.process_iter():
        try:
            if name.lower() in proc.name().lower():
                pids.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pids

def open_helium(instance_count = 1):
    for i in range(instance_count):
        print("Opening " + app_name)
        os.system(f"open -n {app_name}.app")
        

def print_and_wait_countdown(waitTime):
    print("You have " + str(waitTime) + "seconds")
    for i in reversed(range(waitTime)):
      time.sleep(1)
      print(str(i) + "...")

def bring_to_front(pids):
    for i in pids:
        time.sleep(1)
        x = NSRunningApplication.runningApplicationWithProcessIdentifier_(i)
        x.hide()
        time.sleep(1)

        x.unhide()
        print(f"PID {i} was unhid!")

run()