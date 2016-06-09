import sys, os
import mimetypes



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

	#f = open(sys.argv[1])

	for f in get_filepaths(sys.argv[1]):
		if mimetypes.guess_type(f)[0] == 'text/plain':
			#print(f)
			init = open(f)
			print ("Opening the file: " + f)
			target = open(f[:-3]+"fa", 'w')
			i = 0
			while True:
				i += 1
				read = init.readline()
				if read == '':
					break
				target.write(">" + str(i))
				target.write("\n")
				target.write(read.strip())
				target.write("\n")
			target.close()
			init.close()
			os.system("perl fasta_to_fastq.pl " + f[:-3]+"fa >" + f[:-3]+"fq")

