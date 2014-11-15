processmonitor
==============
shows the average memory use and the combined cpu usage for multiple worker 
processes.  this is useful to track the health of the worker processes of
apache or nginx.

how it works
------------
the worker PIDs are found for the process named in the command line.  
the resident set size and the virtual memory size is the average of all the worker PIDs.  
the total cpu percent consumed is the sum of the cpu percent consumed for each worker processes.  
the percent cpu consumed is calculated for each PID by examining the system and user cpu cycles consumed at 2 points in time.  
in order to calculate cpu percent used, a small file is written on disk for each worker process.  
the next time the cpu_usage function is called, it compares the current number of cpu cycles consumed with the file on disk, which is the prior number of cpu cycles consumed.  

how to run it
-------------
set up environment:  
`git clone <repo url>`  
`cd processmonitor`  
`virtualenv . --no-site-packages`  
`source bin/activate`  
`pip install -r requirements.txt`  

run program:  
`python process_monitor.py apache 30`  

sample output:
```
('apache', {'rss_ave_mb': 3, 'workers': 3, 'vms_ave_mb': 224}, {})
('apache', {'rss_ave_mb': 3, 'workers': 3, 'vms_ave_mb': 224}, {'total_consumed_user_cycles': 764, 'total_consumed_system_cycles': 1201, 'total_percent_consumed': 64.27766263206821})
('apache', {'rss_ave_mb': 3, 'workers': 3, 'vms_ave_mb': 224}, {'total_consumed_user_cycles': 748, 'total_consumed_system_cycles': 1238, 'total_percent_consumed': 66.01126687283042})
```
