#!/bin/bash

#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v nucleo="$nuc" '/^#/{next} {if ($4 == nucleo) {print $5}}' $1 | sort | uniq -c
done


