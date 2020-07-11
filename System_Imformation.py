import shutil as DI
import psutil as SI

def Check_Disk_Usage(disk):
	du=DI.disk_usage(disk)
	free=du.free/du.total*100
	return free>20

def Check_CPU_Usage():
	usage=SI.cpu_percent(1)
	return usage<75

if not Check_Disk_Usage("/") and not Check_CPU_Usage():
	print("error")
else:
	print("everything is fine")