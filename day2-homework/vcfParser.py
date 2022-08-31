#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    info_description = {}
    info_type = {}
    format_description = {}
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0

    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs):
        if line.startswith("#"):
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                                elif name == "Type":
                                    Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: #not working with headers
            try:
                fields = line.rstrip().split("\t") #removes new line character, splitting where there are tabs creates variable fields which is a list (everything inside is a string)
                fields[1] = int(fields[1]) #second column is now an integer
                if fields[5] != ".": 
                    fields[5] = float(fields[5]) 
                info = {}
                for entry in fields[7].split(";"): #making a list of strings. separating at all the ;
                    temp = entry.split("=") #creating another list of strings ["AC" , "91"]
                    if len(temp) == 1:
                        info[temp[0]] = None #if just AC, we're adding to the info dictionary with key = AC and Value = None
                    else: #this block is saving the name and values to the info dictionary 
                        name, value = temp 
                        Type = info_type[name]
                        info[name] = type_map[Type](value) #type_map is converting the value to the right data type
                fields[7] = info #storing the info dictionary to column 7
                if len(fields) > 8: 
                    fields[8] = fields[8].split(":") #creates list of string
                    if len(fields[8]) > 1: #if we have more than gt 
                        for i in range(9, len(fields)): #we have to do the same split on all the following genetype columns
                            fields[i] = fields[i].split(':')
                    else:
                        fields[8] = fields[8][0] #fields[8] = GT
                vcf.append(fields)
            except: #if any of the preceding code failed
                malformed += 1 #note that there was a malformed line
    vcf[0][7] = info_description #update vcf list with info we got from info line and format description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    return vcf

if __name__ == "__main__": #if command line script name matches this script name
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
