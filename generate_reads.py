import sys, os

prog_path = "go run edmulti.go "
chr_fasta_path = "/backup2/nsvo/variant_calling/Human_data/refs/GRCh37_"
snp_vcf_path = "/backup2/nsvo/variant_calling/Human_data/refs/TRIMMED.ALL."
				#chr1.integrated_phase1_v3.20101123.snps_indels_svs.genotypes.vcf
outs = " outs/"
outreads = " reads50/"

fq_list_fn = sys.argv[1]
flank_extent = sys.argv[2]


if __name__ == '__main__':

	print ("Generate reads from Optimal Alignments")

	f = open(fq_list_fn)
	while True:
		fname = f.readline().strip()
		if fname == '':
			break

		cmd = prog_path+chr_fasta_path+fname[:-3]+".fasta "+snp_vcf_path+fname[:-3]+".integrated_phase1_v3.20101123.snps_indels_svs.genotypes.vcf "+flank_extent+outs+fname[:-3]+outreads+fname[:-3]
		print(cmd)
		#os.system(cmd)		

	print ("#######################################")
