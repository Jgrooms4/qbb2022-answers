1. 
A. 
0.55 is the starting point (inclusive)
1.05 is the ending point (exclusive)
0.05 is the interval change
creates a list of 10 values ranging from 0.55 to 1.05

numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)) does not alter the initial array because the integers in the initial array only include 2 decimals

using [::-1] in numpy.around reverses the order of the list items

D. 
This study was focused on the biological phenomena "transmission distortion" wherein certain alleles are transmitted to offspring higher than the expected rate of 50%.
This study is similar to my simulation because the expected probability is 50 percent in both cases. This study differs from my simulation because it accounts for the confounding factors which aren't present in a simple coin-flip simulation. Many more factors can potentially affect the outcome in allele inheritance than in coin flips. The 'probability of heads' parameter in my simulation corresponds to the transmission rate in the paper and the 'number of tosses' corresponds to the number of sperm axis. Both cases used a binomial test because we wanted to know if the results (coin toss result or allele transmission) significantly deviated from the expected outcome - that both possible outcomes (heads/tails or maternal/paternal alleles) had equal likelihoods of occurrence. 