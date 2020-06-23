filex = open(r'C:\Users\Hugo\Desktop\1ºano\2ºSemestre\Métodos Estatísticos\introduction-datascience-python-book-master\files\ch03\adult.data', 'r')

def chr_int(a):
    if a.isdigit():
        return int(a)
    else:
        return 0
                
data=[]
for line in filex:
     data1=line.split(', ')
     if len(data1)==15:
        data.append([chr_int(data1[0]),data1[1],chr_int(data1[2]),data1[3],chr_int(data1[4]),data1[5],data1[6],\
            data1[7],data1[8],data1[9],chr_int(data1[10]),chr_int(data1[11]),chr_int(data1[12]),data1[13],\
            data1[14]])

#print(data[1:2])


import pandas as pd

df = pd.DataFrame(data) #  Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes 

df.columns = ['age', 'type_employer', 'fnlwgt', 'education', 
                "education_num","marital", "occupation", "relationship", "race","sex",
                "capital_gain", "capital_loss", "hr_per_week","country","income"]
#print(df.head())
#print(df.tail())
#print(df.shape)

counts = df.groupby('country').size()

#print(counts) 
# also: df.outcome.value_counts()

counts = df.groupby('age').size() # grouping by age
#print(counts) 


ml = df[(df.sex == 'Male')] # grouping by sex
#print(ml.shape)

ml1 = df[(df.sex == 'Male')&(df.income=='>50K\n')]
#print(ml1.shape)

fm =df[(df.sex == 'Female')]
#print(fm.shape)

fm1 =df[(df.sex == 'Female')&(df.income=='>50K\n')]
#print(fm1.shape)

df1=df[(df.income=='>50K\n')]

#print('The rate of people with high income is: ', int(len(df1)/float(len(df))*100), '%.') 
#print('The rate of men with high income is: ', int(len(ml1)/float(len(ml))*100), '%.' )
#print('The rate of women with high income is: ', int(len(fm1)/float(len(fm))*100), '%.') 

#print ('The average age of men is: ', ml['age'].mean(), '.') 
#print ('The average age of women is: ', fm['age'].mean(), '.')

#print ('The average age of high-income men is: ', ml1['age'].mean(), '.') 
#print ('The average age of high-income women is: ', fm1['age'].mean(), '.')

ml_mu = ml['age'].mean()
fm_mu = fm['age'].mean()
ml_var = ml['age'].var()
fm_var = fm['age'].var()
ml_std = ml['age'].std()
fm_std = fm['age'].std()
#print ('Statistics of age for men: mu:', ml_mu, 'var:', ml_var, 'std:', ml_std)
#print ('Statistics of age for women: mu:', fm_mu, 'var:', fm_var, 'std:', fm_std)

ml_mu_hr = ml['hr_per_week'].mean()
fm_mu_hr = fm['hr_per_week'].mean()
ml_var_hr = ml['hr_per_week'].var()
fm_var_hr = fm['hr_per_week'].var()
ml_std_hr = ml['hr_per_week'].std()
fm_std_hr = fm['hr_per_week'].std()
#print ('Statistics of hours per week for men: mu:', ml_mu_hr, 'var:', ml_var_hr, 'std:', ml_std_hr)
#print ('Statistics  of hours per week for women: mu:', fm_mu_hr, 'var:', fm_var_hr, 'std:', fm_std_hr)

ml_median= ml['age'].median()
fm_median= fm['age'].median()
#print ("Median age per men and women: ", ml_median, fm_median)

ml_median_age= ml1['age'].median()
fm_median_age= fm1['age'].median()
#print ("Median age per men and women with high-income: ", ml_median_age, fm_median_age)

ml_median_hr= ml['hr_per_week'].median()
fm_median_hr= fm['hr_per_week'].median()
#print ("Median hours per week per men and women: ", ml_median_hr, fm_median_hr)

import matplotlib.pyplot as plt


ml_age=ml['age']
"""
ml_age.hist(normed=0, histtype='stepfilled', bins=20)

plt.xlabel('Age',fontsize=15)
plt.ylabel('Male samples',fontsize=15)
print(plt.show())


"""
fm_age=fm['age']

"""
fm_age.hist(normed=0, histtype='stepfilled', bins=10)
plt.xlabel('Age',fontsize=15)
plt.ylabel('Female samples',fontsize=15)
print(plt.show())
"""

import seaborn as sns
"""
fm_age.hist(normed=0, histtype='stepfilled', alpha=.5, bins=20)   # default number of bins = 10
ml_age.hist(normed=0, histtype='stepfilled', alpha=.5, color=sns.desaturate("indianred", .75), bins=10)
plt.xlabel('Age',fontsize=15)
plt.ylabel('Samples',fontsize=15)
print(plt.show())
"""
"""
fm_age.hist(normed=1, histtype='stepfilled', alpha=.5, bins=20)   # default number of bins = 10
ml_age.hist(normed=1, histtype='stepfilled', alpha=.5, color=sns.desaturate("indianred", .75), bins=10)
plt.xlabel('Age',fontsize=15)
plt.ylabel('PMF',fontsize=15)
print(plt.show())
"""
"""
ml_age.hist(normed=1, histtype='stepfilled', bins=20)
plt.xlabel('Age',fontsize=15)
plt.ylabel('Probability',fontsize=15)
print(plt.show())
"""
"""
fm_age.hist(normed=1, histtype='stepfilled', bins=20)
plt.xlabel('Age',fontsize=15)
plt.ylabel('Probability',fontsize=15)
print(plt.show())
"""
"""
ml_age.hist(normed=1, histtype='step', cumulative=True, linewidth=3.5, bins=20)
plt.xlabel('Age',fontsize=15)
plt.ylabel('CDF',fontsize=15)
print(plt.show())
"""
"""
fm_age.hist(normed=1, histtype='step', cumulative=True, linewidth=3.5, bins=20)
plt.xlabel('Age',fontsize=15)
plt.ylabel('CDF',fontsize=15)
print(plt.show())
"""
"""
ml_age.hist(bins=10, normed=1, histtype='stepfilled', alpha=.5)   # default number of bins = 10
fm_age.hist(bins=10, normed=1, histtype='stepfilled', alpha=.5, color=sns.desaturate("indianred", .75))
plt.xlabel('Age',fontsize=15)
plt.ylabel('Probability',fontsize=15)
print(plt.show())
"""
"""
ml_age.hist(normed=1, histtype='step', cumulative=True,  linewidth=3.5, bins=20)
fm_age.hist(normed=1, histtype='step', cumulative=True,  linewidth=3.5, bins=20, color=sns.desaturate("indianred", .75))
plt.xlabel('Age',fontsize=15)
plt.ylabel('CDF',fontsize=15)
print(plt.show())
"""

#print ("The mean sample difference is ", ml_age.mean() - fm_age.mean())

#print(df['age'].median())

#print(len(df[(df.income == '>50K\n') & (df['age'] < df['age'].median() - 15)]))
#print(len(df[(df.income == '>50K\n') & (df['age'] > df['age'].median() + 35)]))

df2 = df.drop(df.index[(df.income=='>50K\n') & (df['age']>df['age'].median() + 35) & (df['age'] > df['age'].median() -15)])
print(df2.shape)

ml1_age=ml1['age']
fm1_age=fm1['age']

ml2_age = ml1_age.drop(ml1_age.index[(ml1_age > df['age'].median() + 35) & (ml1_age > df['age'].median() - 15)])
fm2_age = fm1_age.drop(fm1_age.index[(fm1_age > df['age'].median() + 35) & (fm1_age > df['age'].median() - 15)])

mu2ml = ml2_age.mean()
std2ml = ml2_age.std()
md2ml = ml2_age.median()
# Computing the mean, std, median, min and max for the high-income male population
print("Men statistics: Mean:", mu2ml, "Std:", std2ml, "Median:", md2ml, "Min:", ml2_age.min(), "Max:", ml2_age.max())

mu3ml = fm2_age.mean()
std3ml = fm2_age.std()
md3ml = fm2_age.median()
# Computing the mean, std, median, min and max for the high-income female population
print("Women statistics: Mean:", mu2ml, "Std:", std2ml, "Median:", md2ml, "Min:", fm2_age.min(), "Max:", fm2_age.max())

print ('The mean difference with outliers is: %4.2f.' % (ml_age.mean() - fm_age.mean()))
print ("The mean difference without outliers is: %4.2f." % (ml2_age.mean() - fm2_age.mean()))

plt.figure(figsize=(13.4,5))

df.age[(df.income == '>50K\n')].plot(alpha=.25, color='blue')
df2.age[(df2.income == '>50K\n')].plot(alpha=.45,color='red')

print(plt.ylabel('Age'))
print(plt.xlabel('Samples'))

import numpy as np

countx,divisionx = np.histogram(ml2_age, normed=True)
county,divisiony = np.histogram(fm2_age, normed=True)

import matplotlib.pyplot as plt

val = [(divisionx[i]+divisionx[i+1])/2 for i in range(len(divisionx)-1)]
plt.plot(val, countx-county, 'o-') 
plt.title('Differences in promoting men vs. women')
plt.xlabel('Age',fontsize=15)
plt.ylabel('Differences',fontsize=15)
#print(plt.show())

print "Remember:\n We have the following mean values for men, women and the difference:\nOriginally: ", ml_age.mean(), fm_age.mean(),  ml_age.mean()- fm_age.mean() # The difference between the mean values of male and female populations.
print "For high-income: ", ml1_age.mean(), fm1_age.mean(), ml1_age.mean()- fm1_age.mean() # The difference between the mean values of male and female populations.
print "After cleaning: ", ml2_age.mean(), fm2_age.mean(), ml2_age.mean()- fm2_age.mean() # The difference between the mean values of male and female populations.

print "\nThe same for the median:"
print ml_age.median(), fm_age.median(), ml_age.median()- fm_age.median() # The difference between the mean values of male and female populations.
print ml1_age.median(), fm1_age.median(), ml1_age.median()- fm1_age.median() # The difference between the mean values of male and female populations.
print ml2_age.median(), fm2_age.median(), ml2_age.median()- fm2_age.median(), # The difference between the mean values of male and female populations.
