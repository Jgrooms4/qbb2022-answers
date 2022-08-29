# QBB2022 repository
 # QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn UNIX

2. 
a. 
cp genes.chr21.bed ~/qbb2022-answers/day1-lunch
cp exons.chr21.bed ~/qbb2022-answers/day1-lunch

b.
wc genes.chr21.bed 
     219     657    5256 genes.chr21.bed
	 
wc exons.chr21.bed 
	13653   40959  327672 exons.chr21.bed
	
python
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 13653 // 219
62
62 exons per gene

c. 
I would create a fourth column that subtracts the start position from the end position. I would then sort the fourth column, and use the head function to print the (13653/2) position

3.
a. 
cp chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed ~/qbb2022-answers/day1-lunch
b. 
cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq -c
 305 1
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
c. state 7 has the highest count

4. 
a.
cp integrated_call_samples.panel ~/qbb2022-answers/day1-lunch/

b.
grep AFR integrated_call_samples.panel | cut -f 2 | sort | uniq -c
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI

c. I would use the grep function for the other super populations, and keep the remaining code the same

5. 
a. 
cp random_snippet.vcf ~/qbb2022-answers/day1-lunch/

cut -f 10 HG00100.txt | sort | uniq -c
 79 0|0
   1 1|1






	 