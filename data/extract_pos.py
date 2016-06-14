#extract indel pos from outchr
import sys, os

if __name__ == '__main__':

	f = open(sys.argv[1])
	c = 0
	while True:
		line = f.readline()
		if line == '':
			break
		#print(line)
		c += 1
		if (c % 3 == 1):
			sl = line.split()
			print(sl[0])
