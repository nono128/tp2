#Config : Différentes fonctions du programme
import os, psutil, socket

def ip_and_host():
	hostname = socket.gethostname()

	print(f"Hostname: {hostname}")


def cpu():
	load1, load5, load15 = psutil.getloadavg()
	cpu_usage = (load15/os.cpu_count()) * 100

	print("The CPU usage is : ", cpu_usage, "%")


def ram():
	print('RAM memory % used:', psutil.virtual_memory()[2], "%")

