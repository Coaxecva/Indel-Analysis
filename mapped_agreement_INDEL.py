import sys, os

folder_fq_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads/"
folder_sam_path = "/home/qmtran/Indel_Analysis/Data_reads22_29/reads/alignment/"
flank_match = "21M"

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
	alist = ["Bowtie2.", "SHRiMP.", "Razers3.", "Cushaw2.", "Bwasw.", "Gassst.", "Smalt."]
	for f in open(fq_list_fn):		
		total = sum(1 for line in open(folder_fq_path + f.strip()))				
		for aligner in alist:
			#print(aligner)
			agreement = 0
			mapped = 0
			for line in open(folder_sam_path + f[:-3] + aligner + "sam"):
				if line[0] == "@":
					pass
				else:
					sl = line.split()
					print(sl)
					#print(int(sl[0][sl[0].find("##")+2:])-int(flank_match[:-1])) #true pos
					#print(sl[3]) #estimate
					if (abs(int(sl[0][sl[0].find("##")+2:])-int(flank_match[:-1])-int(sl[3])) < allowed_dis):
						mapped += 1
						#print("++")
					cigar = sl[5]					
					if (cigar[:3]==flank_match):
						agreement += 1
			print(str(total/4)+"\t"+str(mapped)+"\t"+str(agreement))
			exit()

	print ("###########################################################")
	
