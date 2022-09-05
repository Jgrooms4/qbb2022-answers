#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1"\t"$2-1"\t"$2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed

#skip header prints column 1 (chromosome), position before SNP, and column 2 (position)
#sorts genes by chromosome and starting position
#finds variant closest to each gene

