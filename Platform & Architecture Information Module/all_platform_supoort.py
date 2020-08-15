"""Below User defined module contains below methods as
CPU_Info_OS() : Displays information of CPU depending on OS
Platform_Info() : Display information of Platform (Operating System)
Boot_Info() : Display boot time of machine
CPU_Info() : Display all information of CPU
RAM_Usage() : Display information of RAM usage
Disk_Info() : Display information of Hard disk"""

"""psutil (python system and process utilities) is a cross-platform library for retrieving information 
on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful
 mainly for system monitoring, profiling, limiting process resources and the management of running processes."""

import psutil

#The Platform module is used to retrieve as much possible information about the platform on which the program is
# being currently executed

import platform

#The OS module in python provides functions for interacting with the operating system. OS, comes under Python's standard
# utility modules. This module provides a portable way of using operating system dependent functionality

from os import *

from datetime import datetime

def CPU_INFO_OS():
    print("CPU info OS")

    if platform.os == "Windows":
        return platform.processor()
    elif platform.system() == "linux":
        command='cat/proc/cpuinfo'
        return popen(command).read().strip()
    else:
        return 'platform not identified'

def get_size(bytes,suffix="B"):
    factor=1024
    for unit in ["","K","M","G","T","P"]:
        if bytes<factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes/=factor

def Platform_Info():
    uname=platform.uname()
    print(f"System: {uname.system}")
    print(f"Release: {uname.release}")
    print(f"SNode name: {uname.node}")
    print(f"version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def boot_info():
    boot_time_timestamp=psutil.boot_time()
    bt=datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot time {bt.year}/{bt.month}/{bt.day} {bt.hour} : {bt.minute} : {bt.second}")


def cpu_info():
    print("pysical core :",psutil.cpu_count(logical= False))
    print("Total / logical cores :" , psutil.cpu_count())



CPU_INFO_OS()
Platform_Info()
boot_info()
cpu_info()