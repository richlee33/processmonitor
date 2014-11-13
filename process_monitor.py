import sys
import time
import get_pids
import memory_stats
import cpu_stats

#process = 'apache'

process = str(sys.argv[1])

while True:
    list_pids = get_pids.get_pids(process)
    # print (list_pids)
    mem =  memory_stats.memory_average(list_pids)
    cpu = cpu_stats.cpu_usage(list_pids)
    print (process, mem, cpu )
    print '================================='
    time.sleep(30)

