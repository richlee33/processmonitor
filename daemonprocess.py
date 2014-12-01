import sys
import psutil

class DaemonProcess:

    #daemon is started by the init process so has the parent PID of 1
    daemon_parent_pid = 1

    def __init__(self, *args):
        if len(args) > 0: 
            self.set_process_name(args[0])
      

    def set_process_name(self, process_name):
   
        if len(process_name) == 0:
            self.process_name = None
        else:
            self.process_name = process_name

        return


    def find_daemon_pid(self):
    #finds the PID of the daemon/parent process.
    #input: daemonprocess instance
    #output: int for parent PID
    
        daemon_pid = -1

        for p in psutil.process_iter():
            if (p.ppid() == self.daemon_parent_pid 
            and (self.process_name in p.name())):
                daemon_pid = p.pid
                break

        if daemon_pid < 0: 
            print 'daemon ' + self.process_name + ' not found'
            daemon_pid = None 

        return daemon_pid


    def find_worker_pid(self):
    #finds PID(s) of the worker process spawned by the daemon PID.
    #input: daemon process instance 
    #output: list of worker PIDs
        
        daemon_pid = self.find_daemon_pid()

        if daemon_pid == None:
            return None

        worker_pid = []
    
        for p in psutil.process_iter():
           if p.ppid() == daemon_pid:
                worker_pid.append(p.pid)

        if len(worker_pid) == 0:
            print 'daemon PID ' + str(daemon_pid) + ' has no worker processes'

        return worker_pid

