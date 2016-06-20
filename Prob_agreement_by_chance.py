import sys, os

flank_match = "51M"
allowed_dis = 20

outs_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/outs50/"
fq_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads50/"
sam_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads50/alignment/"

fq_list_fn = sys.argv[1]

if __name__ == '__main__':

	print ("###########################################################")
	print ("Prob. of agreement by chance ")
	print ("###########################################################")

	#alist = ["Bowtie2."]
	#alist = ["SHRiMP."]
	#alist = ["Razers3."]
	#alist = ["Cushaw2."]
	#alist = ["Bwasw."]
	#alist = ["Bwamem."]
	#alist = ["Bwa."]
	#alist = ["Gassst."]
	#alist = ["Smalt."]
	alist = ["Bowtie2.", "SHRiMP.", "Razers3.", "Cushaw2.", "Bwasw.", "Bwamem.", "Bwa.", "Gassst.", "Smalt."]

	for f in open(fq_list_fn):		
		total = sum(1 for line in open(fq_path + f.strip()))				
		idx = -1
		for aligner in alist:
			idx += 1
			#print(aligner)
			agreement = 0
			mapped = 0
			for line in open(sam_path + f[:-3] + aligner + "sam"):
				if line[0] == "@":
					pass
				else:
					sl = line.split()
					#print(f)
					#print(sl)
					#print(int(sl[0][sl[0].find("##")+2:])-int(flank_match[:-1])) #true pos
					#print(sl[3]) #estimate
					if (sl[3] == ''):
						continue

			print(str(total/4))

	print ("###########################################################")
