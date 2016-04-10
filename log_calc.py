# Script for logging data from 1-wire counter.
import time

datafile = '/mnt/1wire/uncached/1D.010D0D000000/counter.A'
logfile = '/home/fredde/log_calc.csv'
pulses = 500. # Number of pulses per kWh
c2 = 0
energy = 0
t2 = time.time()+1

print "Starting counter log..."

while True:
	t1 = time.time()
	tid = str(time.localtime()[0])+','+str(time.localtime()[1])+','+str(time.localtime()[2])+','+str(time.localtime()[3])+','+str(time.localtime()[4])+','+str(time.localtime()[5])
	with open(datafile, 'r') as c:
		counter_read = c.read()
	c.closed
	if int(c2) < int(counter_read):
		energy = (float(counter_read)-float(c2)) / pulses
		power = (energy * 3600) / (t1 - t2)
		with open(logfile, 'a') as w:
			w.write(str(t1)+','+tid+','+counter_read+','+str(energy)+','+str(power)+'\n')
		w.closed
		c2 = counter_read
		t2 = t1