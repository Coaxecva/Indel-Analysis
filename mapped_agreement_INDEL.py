import sys, os

folder_fq_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads50/"
folder_sam_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads50/alignment/"
flank_match = "51M"

allowed_dis = 20

fq_list_fn = sys.argv[1]

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


if __name__ == '__main__':

	print ("###########################################################")

	
	#Stat:	
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
	Indel_Pos = [set() for _ in alist]

	for f in open(fq_list_fn):		
		total = sum(1 for line in open(folder_fq_path + f.strip()))				
		idx = -1
		for aligner in alist:
			idx += 1
			#print(aligner)
			agreement = 0
			mapped = 0
			for line in open(folder_sam_path + f[:-3] + aligner + "sam"):
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
						#print("++")
						#cigar = sl[5]					
						#print(cigar[:3], flank_match)
						#if (cigar[:3]==flank_match):
							#agreement += 1	
					#print(sl[5])
					if (sl[5] == '*'):
						continue
					#print(abs(int(sl[0][sl[0].find("##")+2:])-int(sl[3])))
					#print(sl[5][:(sl[5].find('M'))])
					if(sl[5].find('M') > 2):
						continue
					if (abs(int(sl[0][sl[0].find("##")+2:])-int(sl[3])) == int(sl[5][:(sl[5].find('M'))])-1):
						agreement += 1	
						#print(idx)
						Indel_Pos[idx].add(sl[3])

			print(str(total/4)+"\t"+str(mapped)+"\t"+str(agreement))
	
	#Venn diagram
	print("-----------------")
	
	print(len(Indel_Pos[0]-Indel_Pos[1]-Indel_Pos[5])) # A-B-C
	print(len(Indel_Pos[5]-Indel_Pos[0]-Indel_Pos[1])) # C-A-B
	print(len(Indel_Pos[1]-Indel_Pos[0]-Indel_Pos[5])) # B-A-C
	print(len(Indel_Pos[0]&Indel_Pos[5]-Indel_Pos[1])) # A&C-B
	print(len(Indel_Pos[5]&Indel_Pos[1]-Indel_Pos[0])) # C&B-A
	print(len(Indel_Pos[0]&Indel_Pos[1]-Indel_Pos[5])) # A&B-C
	print(len(Indel_Pos[0]&Indel_Pos[1]&Indel_Pos[5])) # A&B&C

	print(len(Indel_Pos[2]-Indel_Pos[3])) # D-E
	print(len(Indel_Pos[2]&Indel_Pos[3])) # D&E
	print(len(Indel_Pos[3]-Indel_Pos[2])) # E-D

	print(len(Indel_Pos[7]-Indel_Pos[8])) # D-E
	print(len(Indel_Pos[7]&Indel_Pos[8])) # D&E
	print(len(Indel_Pos[8]-Indel_Pos[7])) # E-D	

	t1 = Indel_Pos[0]&Indel_Pos[1]&Indel_Pos[5]
	t2 = Indel_Pos[2]&Indel_Pos[3]
	t3 = Indel_Pos[8]-Indel_Pos[7]

	print(len(t1-t2-t3)) # A-B-C
	print(len(t3-t1-t2)) # C-A-B
	print(len(t2-t1-t3)) # B-A-C
	print(len(t1&t3-t2)) # A&C-B
	print(len(t3&t2-t1)) # C&B-A
	print(len(t1&t2-t3)) # A&B-C
	print(len(t1&t2&t3)) # A&B&C

	print ("###########################################################")
	
