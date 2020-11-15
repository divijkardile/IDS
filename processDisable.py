import subprocess
from time import sleep

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

while True:
    print(si)
    subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo = si)
    sleep(1)
    print("Task manager disable")
