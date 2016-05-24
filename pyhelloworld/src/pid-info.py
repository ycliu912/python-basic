#!/usr/bin/env python
#conding=utf-8

import os
from subprocess import Popen
import commands
import sys
import cmd
import time


def get_Pid(process_name):
    cmd = "ps -C %s | grep -v CMD | awk '{print $1}'"%process_name
    try:
        pid = os.popen(cmd).read()
        if pid:
            print 'The  pid of process_name:'%process_name + 'is',pid
            return pid
        else:
            print 'sorre to get pid,maybe the process_name is wrong?'
            exit(1)
    except Exception,e:
        print e
        return pid
def get_Mem(pid):
    cmd_top = 'top -p %s -b -n 1 | tail -n 2 | head -n 1'%pid
    mem = os.popen(cmd_top).read().split()[4]
    return mem

def pid_status(process_name):
    PID = get_Pid(process_name)
    print "get_Pid(process_name) = ",PID
    cmd_pid_status = 'lsof -p %s'%PID
    #print "cmd_pid_status = ",cmd_pid_status
   # pid_status01 = os.system(cmd_pid_status)
    pid_status01 = os.popen(cmd_pid_status).read()
    #pid_status01 = commands.getoutput('lsof -p %s | wc -l' % (PID))
    print "pid_status01 = ",pid_status01
    return "pid_status01",pid_status01
    

def get_pid_status(process_name):
    pid_status02 = pid_status(process_name)
    while (pid_status02 > 0):
        print "'%s' is on running!"%process_name
        time.sleep(3)
        pid_status02 = pid_status(process_name)
        if (pid_status02 <= 0):
            print "'%s' has been stopped."
            break
        continue
        

def main(process_name):
    PID = get_Pid(process_name)
    #result = get_Mem(PID)
    #print "the process '%s',whose mem is %s"%(process_name,result)
    print "the process '%s' pid = '%s'"%(process_name,PID)
    get_pid_status(process_name) 

if __name__=='__main__':
    process_name = sys.argv[1]
    main(process_name)