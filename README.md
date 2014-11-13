processmonitor
==============
shows the average memory use and the combined cpu usage for multiple worker 
processes.  this is useful to track the health of the worker processes of
apache or nginx.

how it works
------------

how to run it
-------------
set up environment:  
`git clone <repo url>`  
`cd processmonitor`  
`virtualenv . --no-site-packages`  
`source bin/activate`  
`pip install -r requirements.txt`  

run program:  
`python process_monitor.py apache`  

