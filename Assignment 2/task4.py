import psutil
import datetime


input =raw_input("Enter pid of running processes , (SPACE SEPERATED)")
input=input.split(' ')

for pid in input:
    try:
        pid=int(pid)
        process = psutil.Process(pid)
        print "Process Id : " , process.pid
        print "Process Name : ",process.name()
        print "Process Status : ",process.status()
        print "Process Parent : ",process._ppid
        print "Process Creation Time : ",datetime.datetime.fromtimestamp(process.create_time()).strftime("%a,%b,%d  %I:%M:%S %Y")
        print "Files Opened : ",process.open_files()
        print "Process Memory Info :",process.memory_info()
        print "Process CPU Usage :", process.cpu_percent()
        print "\n\n"
    except:
        print "No such process found with pid : ",int(pid)


