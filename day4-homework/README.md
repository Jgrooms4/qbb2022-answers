1. 
A. 
0.55 is the starting point (inclusive)
1.05 is the ending point (exclusive)
0.05 is the interval change
creates a list of 10 values ranging from 0.55 to 1.05

numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)) does not alter the initial array because the integers in the initial array only include 2 decimals

using [::-1] in numpy.around reverses the order of the list items
