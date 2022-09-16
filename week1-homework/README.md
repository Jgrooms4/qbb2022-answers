

Question 2
2.1 grep -c '>' contigs.fasta
4 contigs

2.2 
samtools faidx contigs.fasta 
less -S contigs.fasta.fai 
Lengths of contigs:
105830
47860
41351
39426 

2.3 
Largest contig: 105830 nucleotides 

2.4
The N50 is 47860 
samtools faidx ref.fa 
less ref.fa.fai 
50% ref genome is ~ 165,000
contig 2 will intersect the ref genome, so the N50 is 47860

Question 3
1. The average identity of my assembly relative to the reference is 99.9955%
conda install -c bioconda -y mummer4 -f --force-reinstall
mate /Users/cmdb/miniconda3/bin/dnadiff
dnadiff /users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/contigs.fasta
less out.report


2. 
nucmer /users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/contigs.fasta
mate /Users/cmdb/miniconda3/bin/nucmer*
show-coords -r out.delta > out.coords

/Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/contigs.fasta
NUCMER
>Halomonas NODE_1_length_105830_cov_20.649193 233806 105830
127965 233794 1 105830 1 1 0
0
The length of the longest alignment is the same as the length of the longest contig - 105830 nucleotides. 

3. 
less out.report
There is only one insertion in the contig fasta file

4.1 
less out.coords
 3    26789  |        1    26787  |    26787    26787  |   100.00  | Halomonas    NODE_3_length_41351_cov_20.528098
 26788    40641  |    27498    41351  |    13854    13854  |   100.00  | Halomonas    NODE_3_length_41351_cov_20.528098
The insertion is from position 26787 to 27498. 

4.2 
less out.report
The novel insertion is 712 nucleotides long

4.3 
samtools faidx /users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/contigs.fasta NODE_3_length_41351_cov_20.528098:26787-27498
>NODE_3_length_41351_cov_20.528098:26787-27498
CATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGT
TCTATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCAT
TCATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACG
ACCAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGC
GAGCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATA
GCGCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAAC
GCCGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATG
CTTGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAA
GCTGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATT
CGTACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTG
TCTTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTT
AGAAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGTG

4.4
samtools faidx /users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/contigs.fasta NODE_3_length_41351_cov_20.528098:26787-27498 > contiginsert.fasta

./dna-decode.py --decode -input contiginsert.fasta 
Traceback (most recent call last):
  File "/Users/cmdb/qbb2022-answers/week1-homework/./dna-decode.py", line 8, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

#not sure why I can't decode the message

