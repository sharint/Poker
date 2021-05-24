import ReadCards
import subprocess
import win32api
import win32con
import win32job
import sys



hJob = win32job.CreateJobObject(None, "")
extended_info = win32job.QueryInformationJobObject(hJob, win32job.JobObjectExtendedLimitInformation)
extended_info['BasicLimitInformation']['LimitFlags'] = win32job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
win32job.SetInformationJobObject(hJob, win32job.JobObjectExtendedLimitInformation, extended_info)

child = subprocess.Popen([sys.executable, 'Output.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
# Convert process id to process handle:
perms = win32con.PROCESS_TERMINATE | win32con.PROCESS_SET_QUOTA
hProcess = win32api.OpenProcess(perms, False, child.pid)

win32job.AssignProcessToJobObject(hJob, hProcess)



ReadCards.start()
