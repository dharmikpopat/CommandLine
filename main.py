import os

def fetch(cmd):
	x = os.popen(cmd).read()
	y = x.splitlines()
	return y