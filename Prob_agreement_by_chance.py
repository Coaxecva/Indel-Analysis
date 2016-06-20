import sys, os

outs_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads50/"
sam_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads50/alignment/"

fq_list_fn = sys.argv[1]

if __name__ == '__main__':

	print ("###########################################################")
	print ("Prob. of agreement by chance ")
	print ("###########################################################")

	f = open(fq_list_fn)
	while True:
		fname = f.readline().strip()
		if fname == '':
			break
