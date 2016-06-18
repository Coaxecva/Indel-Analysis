# Indel Analysis

python ../generate_reads.py ../input.txt 50

python ../plain2fa.py ../input.txt

python ../SRalignment_runner.py ../input.txt

python ../mapped_agreement_INDEL.py ../input.txt
