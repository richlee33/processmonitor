import sys
import time
import datetime
import argparse

from daemonprocess import DaemonProcess
import memory_stats
import cpu_stats

parser = argparse.ArgumentParser()
parser.add_argument("process", help="name of worker processes to monitor")
parser.add_argument("frequency", type=int, help="sample frequency in seconds")
args = parser.parse_args()

process_name = args.process
frequency_sec = args.frequency

while True:
    current_time = str(datetime.datetime.now())
    dp = DaemonProcess(process_name)
    list_pids = dp.find_worker_pid()
    mem =  memory_stats.memory_average(list_pids)
    cpu = cpu_stats.cpu_usage(list_pids)
    print current_time, (process_name, mem, cpu)
    time.sleep(frequency_sec)

