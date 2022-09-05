# QBB2022 repository
# QBB2022 - Day 1 - Homework Exercises Submission
1. 
#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v nucleo="$nuc" '/^#/{next} {if ($4 == nucleo) {print $5}}' $1 | sort | uniq -c
done

d) yes, A and C are in the same class of nucleotides, as are G and T

2. 
Promoters are defined by inclusion of 'TSS' in description. 

for promo in 1 2 10 11
do
  awk -v promoter="$promo" '/^#/{next} {if ($4 == promoter) {print }}' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort
done

vcffile=~/data/vcf_files/random_snippet.vcf
promofile=~/qbb2022-answers/day1-homework/promo.bed
bedtools intersect -nonamecheck -a $vcffile -b $promofile > promoterSNP.vcf

bash ex2intersect.sh

less promotersnp.vcf

purines are often substituted with other purines, and pyrimidines are often substituted with other pyrimidines

3. 
#forgot to save error message 1, can't find original script
error message 2: Error: Sorted input specified, but the file variants.bed has the following out of order record

awk '/^#/{next} {print $1"\t"$2-1"\t"$2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed

bash exercise3.sh ~/data/vcf_files/random_snippet.vcf | wc
10293 variants returned. 

bash exercise3.sh ~/data/vcf_files/random_snippet.vcf | cut -f 7 | sort | uniq | wc
200 uniq genes

51.47 variants per gene on average


