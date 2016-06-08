#Optimal Alignment
import pandas
import po
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

df = po.read_csv(args.filename, sep="\t")
df["possiblity"] = 1.0/df["opt_num_1_alignment"]

correctly_mapped = df.query('indel_pos - mapped_pos == 21')
tmp = [ r for r in correctly_mapped.values if r[2].startswith('22') and r[6] > 1 ]

correctly_aligned = pandas.DataFrame(tmp, columns=df.keys())
correctly_aligned["p"] = 1.0/correctly_aligned["opt_num_1_alignment"]
correctly_aligned_by_chr = correctly_aligned[['ChrID','non_gap_num','opt_num_1_alignment', 'possiblity']].groupby('ChrID', sort=False)

print("\t\ttotal\tmapped\taligned\taveragepossible")
print(args.filename,"\t",len(df),"\t",len(correctly_mapped),"\t",len(correctly_aligned), correctly_aligned["possiblity"].mean())

print("\nMean")
print(correctly_aligned_by_chr.mean())

print("\nStandard Dev")
print(correctly_aligned_by_chr.std())
Status API Training Shop Blog About
