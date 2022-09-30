Week 3 HW

bwa index sacCer3.fa

bwa mem -R "@RG\tID:Sample09\tSM:Sample09" -o sample09.sam  sacCer3.fa A01_09.fastq

