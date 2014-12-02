processmonitor
==============
shows the average memory use and the combined cpu usage for multiple worker 
processes.  this is useful to track the health of the worker processes of
apache or nginx.

how it works
------------
worker PIDs are found for the process name passed in via the command line.  
the resident set size and the virtual memory size is the average of those values from the worker PIDs.
the total cpu percent consumed is the sum of all the worker PIDs cpu percent usage.  
the percent cpu consumed is calculated for each PID by examining the system and user cpu cycles consumed at 2 points in time.  
in order to calculate cpu percent used, a small file is written on disk for each worker PID.  
the next time the cpu_usage function is called, it compares the current number of cpu cycles consumed with the prior number of cpu cycles consumed found on disk.

how to run it
-------------
set up environment:  
`git clone <repo url>`  
`cd processmonitor`  
`virtualenv . --no-site-packages`  
`source bin/activate`  
`pip install -r requirements.txt`  

find number of CPUs on system and set in cpu_stats.py  
`$nproc`

run program:  
`python process_monitor.py apache 20`  

sample output:
```
2014-11-15 09:17:25.283539 ('apache', None, None)
2014-11-15 09:17:45.315649 ('apache', {'rss_ave_mb': 1, 'workers': 2, 'vms_ave_mb': 222}, {})
2014-11-15 09:18:05.414884 ('apache', {'rss_ave_mb': 2, 'workers': 2, 'vms_ave_mb': 224}, {'total_consumed_user_cycles': 288, 'total_consumed_system_cycles': 521, 'total_percent_consumed': 39.13132194035224})
```

considerations 
--------------

if the cpu value in proces_monitor.py constantly returns {} then most likely the worker processes are stopping and starting or more frequently than the sampling rate.  
change the frequency sampling rate to a lower number.  
its normal for a new execution of this program to have the cpu value return {} once in the beginning.  


run tests 
------------
`cd processmonitor`  
`py.test ./tests/`  

