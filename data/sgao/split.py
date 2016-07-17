import os
from sys import argv
filename = argv[1]
folder = argv[2]
out = open(filename, 'wb')
for filename in os.listdir(folder):
        print filename
        f = open(folder + filename, 'r')
        i = 0
        for line in f:
            if not i % 3:
		    print line
		    l = line.split('\t')
		    out.write(filename + '\t' + l[0] + '\t' + l[2] + '\t' + l[3] + '\n')
	    i += 1
        f.close()

out.close()
