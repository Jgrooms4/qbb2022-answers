

from vcfParser import *


randsnp = parse_vcf("random_snippet.vcf") #loads random snippet into vcf parser
dbsnp = parse_vcf("dbSNP_snippet.vcf") #loads dbsnp into vcf parser

#for i in randsnp[0:10]:
#    print(i)
    
fs = dbsnp
snp_dict = {}
fss = randsnp
rsnp_dict = {}
#print(fs)
for line in fs:
    #fields = line.strip().split('\t') #separates into list whereever there's a tab
    #fields[1] = int(fields[1]) #converts position into an integer
    position = line[1] #saves position as 'position'
    ident = line[2] #saved ID as 'ident'
    snp_dict[position]=ident #creates snp dictionary using position as key and ID as value
    #dbposition = position
    #dbident = ident
    
    
#for k,v in snp_dict.items():
#    print(k,v)



for line in fss: #for each line in the vcf file
    rposition = line[1] #the position is the second colun
    #rident = line[2] #the ID is the third column
    if rposition in snp_dict: #if the position is in the key of the snp dictionary
        line[2] = snp_dict[rposition] #the third column should become the value from the dbsnp
#=    print(line[0:5])
    
unlabeled = 0
for line in fss:
    #print(line[0:5])
    if line[2] == '.':
        unlabeled += 1
print(unlabeled)
        
print(snp_dict)

#for k,v in rsnp_dict.items():
 #   print(k,v)

    #for line in 


# #key is position, value is ID
# fs=open("dbsnp_snippet.vcf",'r') #creates variable that will open dbsnp file
# fss=open("random_snippet.vcf",'r') #creates variable that will open random snippet file
# snp_dict = {} #creates snp dictionary
# rsnp_dict = {} #creates random snippet dictionary
# for line in fs: #reads dbsnp file line by line
#     if line.startswith("#"):
#         continue #skips header
#     else:
#         fields = line.strip().split('\t') #separates into list whereever there's a tab
#         fields[1] = int(fields[1]) #converts position into an integer
#         position = fields[1] #saves position as 'position'
#         ident = fields[2] #saved ID as 'ident'
#         snp_dict[position]=ident #creates snp dictionary using position as key and ID as value
#         #print(snp_dict)
#         for line in fss:
#             if line.startswith("#"):
#                  continue #skips header
#
#             else:
#                 rfields = line.strip().split('\t') #separates into list whereever there's a tab
#                 rfields[1] = int(rfields[1]) #converts position into integer
#                 if rfields[1] == fields[1]: #if random snippet position is the same as dbsnp position
#                     rfields[2] = fields[2] #store dbsnp ID as random snippet ID
#                 rposition = rfields[1] #random snippet position saved as 'rposition'
#                 rident = rfields[2] #random snippet ID saved is 'rident
#                 rsnp_dict[rposition]=rident #creates random snippet dictionary using position as key and ID as value
#                 if rident != '.': #if the random snippet ID was altered
#                     print(rsnp_dict) #print the dictionary
#                     print(len(rsnp_dict))

#fss=open("random_snippet.vcf",'r') #creates variable that will open random snippet file
#rsnp_dict = {} #creates random snippet dictionary
#for line in fss: #reads random snippet file line by line
#	if line.startswith("#"):
 #		continue #skips header
	
#	else:
#		rfields = line.strip().split('\t') #separates into list whereever there's a tab
#		rfields[1] = int(rfields[1]) #converts position into integer
#		if rfields[1] == fields[1]: #if random snippet position is the same as dbsnp position
#			rfields[2] = fields[2] #store dbsnp ID as random snippet ID
#		rposition = rfields[1] #random snippet position saved as 'rposition'
#		rident = rfields[2] #random snippet ID saved is 'rident
#		rsnp_dict[rposition]=rident #creates random snippet dictionary using position as key and ID as value
#		if rident != '.': #if the random snippet ID was altered
#			print(rsnp_dict) #print the dictionary
#			print(len(rsnp_dict))
		