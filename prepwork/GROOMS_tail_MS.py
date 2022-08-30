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

# This is SOOOO close to being completely right. There are two issues that
# you need to fix. The first is that in order to store the lines when you
# read in the file, you need a list, so it should be "storage = []". Then 
# you would storage.append(line) to store the lines. The second is that you
# try to take the last "n_lines" lines from storage. However, you do it to "line"
# inside the for loop. You need to do this before the for loop. You could 
# either put it into a new list and then go line by line through this new list,
# or, you could take the slice when you call the for loop, like
# "for line in storage[-n_lines:]". Also, slicing using [-n_lines:-1] will leave
# out the last line. Instead, you want [-n_lines:], which implicitly says to
# go through the end of the list. This is the same as [-n_lines:len(storage)].
# Also, for easier to read code, you can include blank lines to break up the
# code into functional blocks. This will help your code to be more readable
# and clearer. Also, you started with good comments, but trailed off. Keep up
# comments. Overall, you're doing great. Keep it up! - Mike