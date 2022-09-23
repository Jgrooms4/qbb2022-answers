from fasta import readFASTA
import numpy as np
import sys

seq = sys.argv[1]
scoring = sys.argv[2]
gap_penalty = float(sys.argv[3])
dest = sys.argv[4]

input_sequences = readFASTA(open(seq))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
# sequence1 = 'TGTTACGG'
# sequence2 = 'GGTTGACTA'
# firstarray = [len(sequence1)+1,len(sequence2)+1]
# firstarray1 = np.array(firstarray)
# secondarray1 = np.array(secondarray)
# print(firstarray1)

F_matrix = np.zeros((len(sequence1) + 1, len(sequence2) + 1))
#print(F_matrix)
match_score = 2
mismatch_score = -1
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i * gap_penalty

for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty
    
for i in range(1,len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
        if sequence1[i-1] == sequence2[j-1]:
            d = F_matrix[i-1,j-1] + match_score
        else: 
            d = F_matrix[i-1,j-1] + mismatch_score
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        
        F_matrix[i,j] = max(d,h,v)

print(F_matrix)

# T_matrix = np.zeros((len(sequence1) + 1, len(sequence2) + 1))


