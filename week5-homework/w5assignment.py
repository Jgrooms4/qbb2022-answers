 Week 5 Read Me
 515  curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/chipseq_data.tar.gz --output chipseq_data.tar.gz
  516  tar xzf chipseq_data.tar.gz
  517  ls
  518  samtools view
  519  samtools view -q 10
  520  samtools view -q 10 D0_H3K27ac_treat.bdg 
  521  samtools view -q 10 D2_Sox2_R1.bam 
  522  macs2
  523  head D2_Sox2_R1.bam 
  524  head
  525  head -k D2_Sox2_R1.bam 
  526  cd ..
  527  mkdir week6-homework
  528  cd week6-homework/
  529  mate w6assignment.py
  530  history
  531  cd ~/qbb2022-answers/week5-homework/
  
  
  532  samtools view -q 10 D2_Sox2_R1.bam > d2s2r1
  533  samtools view -q 10 D2_Sox2_R1_input.bam > d2s2r1input
  534  samtools view -q 10 D2_Sox2_R2.bam > d2s2r2
  535  samtools view -q 10 D2_Sox2_R2_input.bam > d2s2r2input
  536  ls
  537  macs2 
  538  mac2 callpeak
  539  macs2 callpeak
  540  macs2 callpeak d2s2r1 d2s2r1input 
  541  macs2 callpeak -t d2s2r1 -c d2s2r1input 
  542  macs2 callpeak -t d2s2r1 -c d2s2r1input -g 94987271 -B -n Sox2D2R1
  543  macs2 callpeak -t d2s2r2 -c d2s2r2input -g 94987271 -B -n Sox2D2R2
  544  ls
  545  head Sox2D2R1_peaks.narrowPeak 
  546  bedtools intersect Sox2D2R1_peaks.narrowPeak Sox2D2R2_peaks.narrowPeak -wa 
  547  bedtools intersect -a Sox2D2R1_peaks.narrowPeak -b Sox2D2R2_peaks.narrowPeak -wa 
  548  bedtools intersect -a Sox2D2R1_peaks.narrowPeak -b Sox2D2R2_peaks.narrowPeak -wa > Sox2D2
  549  ls
  550  head Sox2D2
  551  wc -l Sox2D2R1_peaks.narrowPeak 
  552  wc -l Sox2D2
  
  bedtools intersect -a Sox2D2 -b D2_Klf4_peaks.bed -wa > Sox2Klf4
wc -l Sox2Klf4 
      41 Sox2Klf4
wc -l D2_Klf4_peaks.bed
      60 D2_Klf4_peaks.bed
      41/60 = 68% 
      
python scale_bdg.py Sox2D2R1_treat_pileup.bdg ScaledSox2
  579  ls 
  580  python scale_bdg.py D2_Klf4_treat.bdg ScaledKlf4
  581  python scale_bdg.py D0_H3K27ac_treat.bdg ScaledH3K27acD0
  582  python scale_bdg.py D2_H3K27ac_treat.bdg ScaledH3K27acD2
  583  ls
  584  awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' ScaledSox2  > CroppedSox2
  585  ls
  586  awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' ScaledKlf4  > CroppedKlf4
  587  awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' ScaledH3K27acD0  > CroppedH3K27acD0
  588  awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' ScaledH3K27acD2  > CroppedH3K27acD2
  
  Motif Discovery 
  conda activate meme
  conda install -c conda-forge openmpi=4.1.4 -y
  ln -s /Users/cmdb/data/genomes/mm10.fa ./
  sort -k 5 -r -n Sox2D2 > Sox2D2column5
  head -n 300 Sox2D2column5 > Sox2D2column5head300
  awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' Sox2D2column5head300 > Sox2D2column5head300awk
  samtools faidx -o Sox2D2peaks mm10.fa -r Sox2D2column5head300awk 
  samtools faidx -o Sox2D2peaks mm10.fa -r Sox2D2column5head300awk 
  meme-chip -maxw 7 Sox2D2peaks -oc Sox2memechip 
  conda activate meme 
  meme-chip -maxw 7 Sox2D2peaks -oc Sox2memechip

 614  cd Sox2memechip/
  615  ls
  616  tomtom combined.meme
  617  tomtom combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
  618  cd ..
  619  ls
  620  cd Sox2memechip/
  621  ls
  622  tar xzf /Users/cmdb/Downloads/motif_databases.12.23.tgz 
  623  tomtom combined.meme /Users/cmdb/Downloads/motif_databases.12.23.tgz 
  624  gunzip /Users/cmdb/Downloads/motif_databases.12.23.tgz 
  625  tomtom combined.meme /Users/cmdb/Downloads/motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme 
  626  grep SOX2 tomtom.tsv > SOX2.tsv 
  627  ls
  628  cd tomtom_out
  629  ls
  630  grep SOX2 tomtom.tsv > SOX2.tsv 
  631  ls
  632  grep KLF4 tomtom.tsv > KLF4.tsv
  633  ls
  634  less SOX2.tsv
  635  less KLF4.tsv
