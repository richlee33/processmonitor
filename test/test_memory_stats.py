import os
import sys
import pytest
import memory_stats

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

def test_empty_list():
    empty_list = []
    stats = memory_stats.memory_average(empty_list)
    assert stats == None

def test_invalid_pid():
    invalid_pid_list = [99999999]
    stats = memory_stats.memory_average(invalid_pid_list)
    assert stats == []

def test_valid_invalid_pid():
    valid_invalid_pid_list = [1,99999999]
    stats = memory_stats.memory_average(valid_invalid_pid_list)
    assert stats == []

def test_number_workers():
    worker_list = [1,2,3]
    stats = memory_stats.memory_average(worker_list)
    assert stats['workers'] == 3

