import sys, os

folder_path = "reads22/alignment/"

sam_fn = sys.argv[1]

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
	
	f = open(sys.argv[1])
	while True:
		read = f.readline()
		if read == '':
			break

		for line in open(sam_fn):
		    if line[0] == "@":
		        pass
		    else:
		        sl = line.split()
		        cigar= sl[5]
		        print(cigar[:3], cigar[:3]=="23M")

	print ("###########################################################")
	
