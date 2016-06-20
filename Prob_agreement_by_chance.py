import sys, os

flank_match = "51M"
allowed_dis = 20

outs_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/outs50/out"
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
		#print(f.strip())

		c = 0
		t = -1
		m = {}
		for outline in open(outs_path+f.strip()[:-3]+".txt"):
			c+=1
			if c%3 == 1 :
				osl = outline.split()
				#print(osl)
				print(osl[3])
				t = int(osl[3])
			if c%3 == 0 :
				#print(outline)
				m[outline.strip()] = t

		print(m)

		#chr_agreed = 0
		chr_mapped = 0
		for aligner in alist:		
			#print(aligner)
			agreed = 0
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

					if (abs(int(sl[0][sl[0].find("##")+2:])-int(flank_match[:-1])-int(sl[3])) < allowed_dis):
						mapped += 1

					if (sl[5] == '*'):
						continue

					if(sl[5].find('M') > 2):
						continue

					if (abs(int(sl[0][sl[0].find("##")+2:])-int(sl[3])) == int(sl[5][:(sl[5].find('M'))])-1):
						agreed += 1

			chr_mapped += mapped
			#chr_agreed += agreed
			
		print(str(total/4)+"\t"+str(1.0/chr_mapped))

	print ("###########################################################")
