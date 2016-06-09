import sys, os

ref_path = "~/Indel_Analysis/"

SRmapper_path = "~/quang/SRmapper0.1.5/align "
SHRiMp_path = "~/quang/SHRiMP_2_2_3/bin/gmapper-ls  --ignore-qvs -o 1 --strata "
Bowtie2_path = "~/quang/bowtie2-2.0.2/bowtie2-align -x "
Cushaw2_path = "~/quang/cushaw2-v2.4.2/cushaw2 align -r "
Gassst_path = "~/quang/Gassst_v1.28/Gassst -d "
Razers3_path = "~/quang/razers3 --unique -of sam -o "
BWASW_path = "~/quang/bwa/bwa bwasw "
Smalt_path = "~/quang/smalt map -o "

if __name__ == '__main__':

	f = open(sys.argv[1])
	while True:
		read = f.readline()
		if read == '':
			break
		#print(read.strip())
		#print(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")
		#os.system(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")
		
		print(SHRiMp_path+read.strip()+" "+ref_path+"GRCh37_"+read[:-4]+".fasta > "+read[:-4]+".SHRiMP.sam")
		os.system(SHRiMp_path+read.strip()+" "+ref_path+"GRCh37_"+read[:-4]+".fasta > "+read[:-4]+".SHRiMP.sam &")

		print(Bowtie2_path+ref_path+"GRCh37_"+read[:-4]+"-bowtie2 "+read.strip()+" -S "+read[:-4]+".Bowtie2.sam")
		os.system(Bowtie2_path+ref_path+"GRCh37_"+read[:-4]+"-bowtie2 "+read.strip()+" -S "+read[:-4]+".Bowtie2.sam")
		
		print(Cushaw2_path+ref_path+"GRCh37_"+read[:-4]+".fasta -f "+read.strip()+" -o "+read[:-4]+".Cushaw2.sam")
		os.system(Cushaw2_path+ref_path+"GRCh37_"+read[:-4]+".fasta -f "+read.strip()+" -o "+read[:-4]+".Cushaw2.sam &")
		
		print(Gassst_path+ref_path+"GRCh37_"+read[:-4]+".fasta -i "+read[:-4]+".fa -o "+read[:-4]+".Gassst -p 90 -h 1 && ~/quang/Gassst_v1.28/gassst_to_sam "+read[:-4]+".Gassst "+read[:-4]+".Gassst.sam")
		os.system(Gassst_path+ref_path+"GRCh37_"+read[:-4]+".fasta -i "+read[:-4]+"fa -o "+read[:-4]+".Gassst -p 90 -h 1 && ~/quang/Gassst_v1.28/gassst_to_sam "+read[:-4]+".Gassst "+read[:-4]+".Gassst.sam &")
		
		print(Razers3_path+read[:-4]+".Razers3.sam "+ref_path+"GRCh37_"+read[:-4]+".fasta "+read.strip())
		os.system(Razers3_path+read[:-4]+".Razers3.sam "+ref_path+"GRCh37_"+read[:-4]+".fasta "+read.strip()+" &")

		print(BWASW_path+ref_path+"GRCh37_"+read[:-4]+".fasta "+read.strip()+" > "+read[:-4]+".Bwasw.sam")
		os.system(BWASW_path+ref_path+"GRCh37_"+read[:-4]+".fasta "+read.strip()+" > "+read[:-4]+".Bwasw.sam &")

		print(Smalt_path+read[:-4]+".Smalt.sam " +ref_path+"GRCh37_"+read[:-4]+".smalt "+read.strip())
		os.system(Smalt_path+read[:-4]+".Smalt.sam " +ref_path+"GRCh37_"+read[:-4]+".smalt "+read.strip()+" &")
		
