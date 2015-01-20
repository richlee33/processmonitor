import os
import sys
import pytest
import mock

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import cpu_stats


@mock.patch('cpu_stats.os.path')
def test_get_cpu_proctable_invalid_pid(mock_os_path):

    #set up the mock
    mock_os_path.isfile.return_value = False

    c_stats = cpu_stats.get_cpu_proctable(1)

    #test that a non existent pid returns empty dictionary
    assert c_stats == {}


@mock.patch('cpu_stats.os.path')
def test_get_cpu_proctable_valid_pid(mock_os_path):

    #set up the mock
    mock_os_path.isfile.return_value = True

    c_stats = cpu_stats.get_cpu_proctable(1)

    #test that the input parameter PID is used to open stat file
    mock_os_path.isfile.assert_called_with('/proc/1/stat')


def test_get_cpu_proctable_read_file():
    data = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'

    with mock.patch('__builtin__.open', mock.mock_open(read_data=data), create=True) as m:
        c_stats = cpu_stats.get_cpu_proctable(1)

        #print m.called
        
        #test that the 14th and 15th values are read from the stat file
        assert (c_stats['user'] == 14) and (c_stats['system'] == 15)
    
