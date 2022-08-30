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
