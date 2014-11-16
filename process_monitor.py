import sys
import time
from datetime import datetime
import argparse

import get_pids
import memory_stats
import cpu_stats

parser = argparse.ArgumentParser()
parser.add_argument("process", help="name of worker processes to monitor")
parser.add_argument("frequency", type=int, help="sample frequency in seconds")
args = parser.parse_args()

process_name = args.process
frequency_sec = args.frequency

while True:
    current_time = str(datetime.now())
    list_pids = get_pids.get_pids(process_name)
    mem =  memory_stats.memory_average(list_pids)
    cpu = cpu_stats.cpu_usage(list_pids)
    print current_time, (process_name, mem, cpu)
    time.sleep(frequency_sec)

