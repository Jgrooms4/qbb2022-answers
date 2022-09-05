1. 
    + Covering 1107407 bp
    + Covering 956640 bp
    + Covering 13780687 bp

cd ~/cmdb-plot-vcfs/
open exons.chr21.bed.vcf.png

cd ~/cmdb-plot-vcfs/cache/
open exons.chr21.bed.vcf.png

confirms images are the same 

transcribed_unprocessed_pseudogene: The gene wasn't unprocessed because it's a pseudogene - there are processed pseudogenes.
transcribed_processed_pseudogene: What are the indicators that turned this gene into a pseudogene?
miRNA: What are the commonalities between miRNA? (my rotation lab will be working with miRNAs)

2. 
Trends among plots: Allele counts between 0-500 comprise a much larger proportion of the SNP-in-individuals population than allele counts >2000. SNPs are quite rare when they occur and happen in differing locations. 

3. 
SYNOPSIS
     bxlab/cmdb-plot-vcfs -- <file1> <file2>

 USAGE
     bash do_all.sh <thing1> <thing2> 

     <_.vcf>   <_.gtf>

 DEPENDENCIES
 python 
 bedtools
 matplotlib
 bash 
 
 DESCRIPTION
     1. Create .bed files for features of interest
         - Run subset_regions.sh Bash script
         - Use grep to select gene types
	2. Create .vcf files for features of interest
		-creates vcf files 
		-prints total sum of length of bp 
	3. Plot the vcf files in a figure 
		-split info column at every ;
		-convert allele count string into an integer 
		-plot AC as x value and AC occurrences as y value 
