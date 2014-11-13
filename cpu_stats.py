import time
import os
import json

def cpu_usage(l):

    cycles_per_sec = 100

    #run $nproc to find number of CPUs
    number_cpus = 1

    #check for an empty list of PIDs
    if len(l) == 0:
        #do nothing and return
        return None

    stats = {'total_percent_consumed' : 0.0,
             'total_consumed_user_cycles' : 0,
             'total_consumed_system_cycles' : 0}

    for pid in l:
        cpu_current = get_cpu_proctable(pid)
        cpu_prior = get_cpu_prior_file(pid)

        if ('timestamp' in cpu_current) and ('timestamp' in cpu_prior) and (len(stats) != 0):
            elapsed_time_sec = cpu_current['timestamp'] - cpu_prior['timestamp']
            consumed_user_cycles = cpu_current['user'] - cpu_prior['user']
            consumed_system_cycles = cpu_current['system'] - cpu_prior['system']
            total_consumed_cycles = consumed_user_cycles + consumed_system_cycles
            available_cycles = elapsed_time_sec * cycles_per_sec * number_cpus
            percent_consumed = total_consumed_cycles / available_cycles * 100
            
            #add up percent used cycles for all process
            stats['total_percent_consumed'] += percent_consumed
            stats['total_consumed_user_cycles'] += consumed_user_cycles
            stats['total_consumed_system_cycles'] += consumed_system_cycles

        else:
            #not able to accurately calculate total_percent_consumed because 
            #either the cpu_current or cpu_prior for the PID is not found.
            #therefore set stats to empty dictionary.
            stats = {}

        write_cpu_file(pid,cpu_current)

    #end for loop
    return stats


def get_cpu_proctable(i):
#gets the consumed user and system cpu cycles for a PID for a point in time
#input: integer representing a PID
#output: dictionary containing consumed user & system cpu cycles and timestamp

    stats = {}
    proc_file = '/proc/' + str(i) + '/stat'

    if os.path.isfile(proc_file):
        current_time = time.time()
        with open(proc_file, 'r') as f:
            content = f.readline()
        parsed = content.split()
        stats['timestamp'] = current_time 
        stats['user'] = int(parsed[13])
        stats['system'] = int(parsed[14])
    else:
        print 'invalid PID, no entry in proctable'

    return stats


def get_cpu_prior_file(i):
#gets the consumed user and system cpu cycles from a prior point in time
#from a file on the file system.
#input: integer representing a PID
#output: dictionary containing consumed user & system cpu cycles and timestamp

    stats = {}
    cpu_file = '/tmp/' + str(i)

    if os.path.isfile(cpu_file):
        with open(cpu_file, 'r') as f:
            stats = json.load(f)
    print stats
    return stats


def write_cpu_file(i,dict_cpu_stats):

    cpu_file = '/tmp/' + str(i)
        
    if ('timestamp' in dict_cpu_stats): 
        f = open(cpu_file, 'w')
        f.write (json.dumps(dict_cpu_stats))
        f.close()

    return

