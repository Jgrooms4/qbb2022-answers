#!/usr/bin/env python

import numpy 
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)
    
#print(numpy.sum(simulate_coin_toss(10)))
    
    #back half
    #print(numpy.sum(simulate_coin_toss(10, seed = 4)))

def correct_pvalues(pvals):
    corrected_pvalues = multipletests(pvals, method="bonferroni")
    return(corrected_pvalues[1])
    
#print(correct_pvalues([0.005, 0.03, 0.04, 0.0003, 0.002]))

def perform_hypothesis_test(n_heads, n_tosses):
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue #grabbing the pvalue attribute from the binom_result instance
    return(pval)
    
#print(perform_hypothesis_test(2, 5))

def interpret_pvalues(pvals):
    interpreted = numpy.array(pvals) < 0.05 
    return(interpreted) #an array of trues and falses
    
#print(interpret_pvalues([0.1, 0.5, 0.05, 0.03, 0.01]))

def compute_power(n_rejected_correctly, n_tests):
    power = n_rejected_correctly / n_tests
    return (power)
    

    
# def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
#     numpy.random.seed(seed)
#     pvals = []
#     power = []
#     tosses = numpy.array([10, 50, 100, 250, 500, 1000])
#     probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
#     for i in range(n_iters): #n iters is how many times we run the simulation
#         results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
#         n_success = numpy.sum(results_arr)
#         pvals.append(perform_hypothesis_test(n_success, n_toss))
#         #list of results, number of heads, list of pvals based on number of heads and tosses
#         for j, itera in tosses:
#             for k, prob in probs
#                 new_twodim_arr[j,k]
#     if correct_the_pvalues:
#         pvals = correct_pvalues(pvals)
#     pvals_translated_to_bools = interpret_pvalues(pvals)
#     powercomp = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
#
#     power.append(powercomp)
#     return(powercomp)
    #return(pvals)
    
# def run_experimenta(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
#     tosses = numpy.array([10, 50, 100, 250, 500, 1000])
#     probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
#     for j, ntoss in enumerate(tosses):
#         for k, nprobs in enumerate(probs):
#             power_mat[ntoss,nprobs]
# #print(power_mat)
#
#
#     numpy.random.seed(seed)
#     pvals = []
#     power = []
#     #tosses = numpy.array([10, 50, 100, 250, 500, 1000])
#     #probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
#     for i in range(n_iters):
#         results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
#         n_success = numpy.sum(results_arr)
#         pvals.append(perform_hypothesis_test(n_success, n_toss))
#         #list of results, number of heads, list of pvals based on number of heads and tosses
#         for j, itera in tosses:
#             for k, prob in probs:
#                 new_twodim_arr[j,k]
#     if correct_the_pvalues:
#         pvals = correct_pvalues(pvals)
#     pvals_translated_to_bools = interpret_pvalues(pvals)
#     powercomp = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
#
#     power.append(powercomp)
#     return(powercomp)
    #return(pvals)
    
#power1 = run_experiment(0.6, 500)
#print(power1)
#power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
#print(power2)

def run_experimenta(n_iters = 100, seed = 389, correct_the_pvalues = False):
	tosses = numpy.array([10, 50, 100, 250, 500, 1000])
	probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
	numpy.random.seed(seed)
	#pvals = []
	power_mat = numpy.zeros((6,10))
	for j, ntoss in enumerate(tosses):
		for k, nprobs in enumerate(probs):
			pvals = [] 
			for m in range(n_iters):
				results_arr = simulate_coin_toss(ntoss, prob_heads = nprobs)
				n_success = numpy.sum(results_arr)
				pvals.append(perform_hypothesis_test(n_success, ntoss))
			if correct_the_pvalues:
				pvals = correct_pvalues(pvals)
			#binom_result = binomtest(n_success, tosses)
			#pval = binom_result.pvalue
			pvals_translated_to_bools = interpret_pvalues(pvals)
			power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
			#return(power)
			power_mat[j, k] = power
            #power_mat.append()
	
	return(power_mat)	

pow_mat = run_experimenta(correct_the_pvalues = True)
pow_mat.astype(float)
#print(pow_mat)
#for ind, line in enumerate(pow_mat):
#line = int(line)
#print(pow_mat)
import seaborn 
print(seaborn.heatmap(pow_mat, vmin=0, vmax=1, cmap="viridis", xticklabels='list-like', yticklabels='list-like'))
#pow_mat.pivot("probs", "tosses")
fig, ax = plt.subplots()
ax = seaborn.heatmap(pow_mat, vmin=0, vmax=1, cmap="viridis", xticklabels='auto', yticklabels='auto')
#ax.set(xticklabels='1, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55')
ax.set_xticklabels(['1','0.95','0.90','0.85','0.80','0.75', '0.70', '0.65', '0.60', '0.55'])
ax.set_yticklabels(['10','50','100','250','500','1000'])
ax.set_ylabel("# of tosses")
ax.set_xlabel("Probability of 'Heads'")
plt.title("Coinflip Heatmap")
#ax = bx.pivot("probs", "tosses")
ax.plot()
fig.savefig("MHTcor.png")
plt.show()

#plt.plot(seaborn.heatmap(pow_mat))
#plt.showfig()
    





#print(run_experiment(0.2, 30, n_iters=5))