''' @author Joseph Milazzo
    @description Upon user locking computer, the script will mute
    system (stop audio service). Upon unlocking, script will un-mute
    system (restart audio service). This assumes user is using Python 2.7,
    Windows, and has Elevated User Rights.
'''
import time
import ctypes
import os
import admin

if not admin.isUserAdmin():
    admin.runAsAdmin()

LOCKED_STATE = 0x010
UNLOCKED_STATE = 0x011
current_state = UNLOCKED_STATE

user32 = ctypes.windll.User32
OpenDesktop = user32.OpenDesktopA
SwitchDesktop = user32.SwitchDesktop
DESKTOP_SWITCHDESKTOP = 0x0100


locked_times = []
prev_time = time.time()

while 1:
    hDesktop = OpenDesktop("default", 0, False, DESKTOP_SWITCHDESKTOP)
    result = SwitchDesktop(hDesktop)
    if current_state is LOCKED_STATE:
        if result:
            #print "unlocked"
            # Turn volume back on
            os.system('net start "Audiosrv"')
            diff = time.time() - prev_time
            #print "Computer locked for ", diff
            locked_times.append(diff)
            break
        else:
            #print time.asctime(), "still locked"
            if len(locked_times) > 0:
                avg = reduce(lambda x, y: x + y, locked_times)/len(locked_times)
            else:
                avg = 2
            time.sleep(avg/3)
    else:
        if not result:
            current_state = LOCKED_STATE
            os.system('net stop "Audiosrv"')
