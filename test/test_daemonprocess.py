import os
import sys
import pytest
import mock

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from daemonprocess import DaemonProcess


def test_set_empty_process_name():
    dp = DaemonProcess('') 
    assert dp.process_name == None


def test_set_process_name():
    dp = DaemonProcess('myprocess')
    assert dp.process_name == 'myprocess'


@mock.patch('daemonprocess.psutil.Process')
@mock.patch('daemonprocess.psutil.process_iter')
def test_find_daemon_pid(mock_process_iter, mock_process):
    process_name = 'myprocess'
    dp = DaemonProcess(process_name)

    #set up mock values
    mock_process.ppid.return_value = 1
    mock_process.pid = 10
    mock_process.name.return_value = 'myprocess'
    mock_process_iter.return_value = [mock_process]

    assert dp.find_daemon_pid() == 10


@mock.patch('daemonprocess.psutil.Process')
@mock.patch('daemonprocess.psutil.process_iter')
def test_find_daemon_pid_no_pid(mock_process_iter, mock_process):
    process_name = 'junk'
    dp = DaemonProcess(process_name)

    #set up mock values
    mock_process.ppid.return_value = 1
    mock_process.pid = 10
    mock_process.name.return_value = 'myprocess'
    mock_process_iter.return_value = [mock_process]

    assert dp.find_daemon_pid() == None


@mock.patch('daemonprocess.psutil.Process')
@mock.patch('daemonprocess.psutil.process_iter')
@mock.patch.object(DaemonProcess, 'find_daemon_pid')
def test_find_worker_pid(mock_find_daemon_pid, mock_process_iter, mock_process):
    process_name = 'myprocess'
    dp = DaemonProcess(process_name)

    #set up mock values
    mock_find_daemon_pid.return_value = 11
    mock_process.ppid.return_value = 11
    mock_process.pid = 100
    mock_process_iter.return_value = [mock_process]

    #find the worker PIDs
    result = dp.find_worker_pid()

    #check that find_worker_pid called find_daemon_pid with no arguements
    mock_find_daemon_pid.assert_called_with()

    #check worker PID 100 is in list
    assert (100 in result)



@mock.patch('daemonprocess.psutil.Process')
@mock.patch('daemonprocess.psutil.process_iter')
@mock.patch.object(DaemonProcess, 'find_daemon_pid')
def test_find_worker_pid_no_daemon(mock_find_daemon_pid, mock_process_iter, mock_process):
    process_name = 'myprocess'
    dp = DaemonProcess(process_name)

    #set up mock values
    mock_find_daemon_pid.return_value = None
    mock_process.ppid.return_value = 88
    mock_process.pid = 100
    mock_process_iter.return_value = [mock_process]

    #find the worker PIDs
    result = dp.find_worker_pid()

    #check that find_worker_pid called find_daemon_pid with no arguements
    mock_find_daemon_pid.assert_called_with()

    #check list is None
    assert result == None
                             
