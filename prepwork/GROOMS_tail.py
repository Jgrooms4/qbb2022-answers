#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #import module
filename = sys.argv[1] #SET input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
  n_lines = int(sys.argv[2]) #SET the desired number of lines
else: #OTHERWISE
  n_lines = 10 #SET the desired number of lines to a default
storage = 0
for index, line in enumerate(open(filename)):
  storage = line
for line in storage:
  line[-n_lines:-1]
  print(line.strip('\r\n')) 
