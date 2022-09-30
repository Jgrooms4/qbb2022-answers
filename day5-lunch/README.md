Exercise 1
python exercise1day5.txt | sort -k 5 > aau1043_dnm_sorted.csv

python exercise1day5b.txt > aau1043_parental_sorted.csv

join aau1043_dnm_sorted.csv /Users/cmdb/qbb2022-answers/aau1043_parental_age.csv 



Exercise 2
2. 

cut -d"," -f 5,6 ~/qbb2022-answers/aau1043_dnm.csv | grep "father" | tr , '\t' | sort -k 1 | uniq -c >> father_counts.txt

sed -i '' 's/,/\t/g' father_counts.txt 

cut -d"," -f 5,6 ~/qbb2022-answers/aau1043_dnm.csv | grep "mother" | tr , '\t' | sort -k 1 | uniq -c >> mother_counts2.txt

The relationship between maternal age and maternally inherited de novo mutations is statistically significant. 
The size of this relationship is 0.3776. 
The relationship between  paternal age and paternally inherited de novo mutations is statistically significant. 
The size of this relationship is  1.3538. 

The number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband, as a t test showed.

The child would be predicted to have 78.018535 de novo mutations if their father was 50.5 at the time of birth

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm #for nnova
from scipy import stats

fam = np.genfromtxt("mf", delimiter = None, dtype = None, encoding = None, names = ["ID", "m_count", "mother", "f_count", "father", "F_age", "M_age"])

print(fam)
print(fam["m_count"])


fig, ax = plt.subplots()
ax.hist(fam["m_count"], alpha = 0.5, label = "maternal mutations")
ax.hist(fam["f_count"], alpha = 0.5, label = "paternal mutations")

#plt.scatter(fam["M_age"], fam["m_count"])
# #ax.hist(df_adelie_f["flipper_length_mm"], alpha = 0.5, label = "female")
ax.set_xlabel("Mutation Count")
ax.set_ylabel("Mutation Count Freq")
ax.legend()
plt.savefig("ex2_c.png")
plt.show()

fig, ax = plt.subplots()
plt.scatter(fam["F_age"], fam["f_count"])
# #ax.hist(df_adelie_f["flipper_length_mm"], alpha = 0.5, label = "female")
ax.set_xlabel("Fathers' Age")
ax.set_ylabel("Mutation Count")
ax.legend()
plt.savefig("ex2_b.png")
plt.show()

model = smf.ols(formula = "f_count ~ 1 + F_age", data = fam)
results = model.fit()
print(results.summary())
print(results.pvalues)

print(results.pvalues)
print(dir(results))\

print(stats.ttest_ind(fam["m_count"],
               fam["f_count"]))

new_data = fam[0]
new_data.fill(0)
new_data['F_age'] = 50.5
print(results.predict(new_data))