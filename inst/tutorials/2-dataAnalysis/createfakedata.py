# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:44:44 2022

@author: soenk
"""

import random as r
from scipy.stats import skewnorm
from scipy.stats import expon
from scipy.stats import pearson3
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import math



l = []

class Participant:
    def __init__(self, sub):
        self.sub = sub;
        self.sex = self.sex_ran();
        self.age = self.age_ran();
        self.gaming = self.gaming_ran();
        self.nationality = "";
        self.schizo_score = self.schizo_ran();
        self.iq = self.iq_ran();
        self.education = self.education_ran();
        self.creat_score = self.creat_ran();
        
    def iq_ran(self):
        return round(r.gauss(105, 15,));
        
    def age_ran(self):
        return round((18 + 6 * (skewnorm.rvs(9, size=1)))[0])
        
    def sex_ran(self):
        sex_list = ["M", "F", "X", "NA"]
        sex_weights = [1, 1, 0.05, 0.01]
        return r.choices(sex_list, sex_weights)[0];

    def gaming_ran(self):
        gaming_list = ["T", "F"]
        gaming_men = [0.7,0.3]
        gaming_women = [0.3, 0.7]
        return r.choices(gaming_list, gaming_men if self.sex == "M" else gaming_women)[0];
    
    def education_ran(self):
        education = "High School";
        ed_factor = r.uniform(0, 1);

        if ed_factor >= .4:
            self.iq += 5;
            if self.age >= 21:
                education = "Undergraduate";
    

        if ed_factor >= .7:
            self.iq += 5;
            if self.age >= 23:
                education = "Graduate";
                
        return education;
    
    def schizo_ran(self):
        return np.clip(round((pearson3.rvs(skew=1, scale=18, size=1, loc=35))[0]),0,100)

    def creat_ran(self):
        creative_score = pearson3.rvs(skew=-0.6, scale=2, size=100000, loc=4.6)[0]
        if self.gaming == "T":
            creative_score += 0.8

        # IQ Effect
        import math
        def sigmoid(x):
            sig = 1 / (1 + math.exp(-x))
            return sig

        creative_score += 3 * sigmoid((self.iq-100)/5) - 1.5

        # Schizo Effect        
        creative_score += -0.8 + 90 * skewnorm.pdf(self.schizo_score, -3, 70, 34)
        return np.clip(round(creative_score), 0, 10);
    
part = []

for i in range(1,2000):
    part.append(Participant(i))

lolz = []

for i in part:
    lolz.append(i.schizo_score)

fig, ax = plt.subplots(1, 1)
ax.hist(lolz, density=True, histtype='stepfilled', alpha=0.2, bins=50)
plt.show()


dat = []
for i in part:
    dat.append([i.sub, i.sex, i.age, i.gaming, i.schizo_score, i.iq, i.education])

import csv

# open the file in the write mode
f = open('user_dat.csv', 'w', newline="")

# create the csv writer
writer = csv.writer(f, delimiter=";")

# write a row to the csv file
writer.writerow(["id", "sex", "age", "gaming", "schizo_Score", "iq", "education"])
writer.writerows(dat,)

# close the file
f.close()


dat = []
for i in part:
    dat.append([i.sub, i.creat_score])

import csv

# open the file in the write mode
f = open('creat_task.csv', 'w', newline="")

# create the csv writer
writer = csv.writer(f, delimiter=";")

# write a row to the csv file
writer.writerow(["id", "creative_task"])
writer.writerows(dat,)

# close the file
f.close()
# =============================================================================
# 
# # Sex   
# 
#     
# sex_list = ["M", "F", "X", "NA"]
# sex_weights = [1, 1, 0.05, 0.01]
# 
# sex = r.choices(sex_list, sex_weights)
# 
# # Gaming
# 
# gaming_list = ["T", "F"]
# gaming_men = [0.7,0.3]
# gaming_women = [0.3, 0.7]
# 
# 
# gaming = r.choices(gaming_list, gaming_men if sex == "M" else gaming_women)
# 
# # Age
# 
# age = round((18 + 6 * (skewnorm.rvs(9, size=1)))[0])
# 
# # IQ
# 
# iq = round(r.gauss(105, 15,));
# 
# # Education
# 
# education = "High School";
# ed_factor = r.uniform(0, 1);
# 
# if ed_factor >= .4:
#     iq += 5;
#     if age >= 21:
#         education = "Undergraduate";
#     
# 
# if ed_factor >= .7:
#     iq += 5;
#     if age >= 23:
#         education = "Graduate";
# 
# # Schizo_Score 0-100
# 
# schizo_score = np.clip(round((pearson3.rvs(skew=1, scale=18, size=1, loc=35))[0]),0,100)
# 
# # Creativity Score - 0-10
# 
# creative_score = pearson3.rvs(skew=-0.6, scale=2, size=100000, loc=4.6)[0]
# 
# # Gaming Effect
# 
# if gaming == "T":
#     creative_score += 0.8
# 
# # IQ Effect
# 
# import math
# 
# def sigmoid(x):
#     sig = 1 / (1 + math.exp(-x))
#     return sig
# 
# 
# 3 * sigmoid((iq-100)/5) - 1.5
# 
# # Schizo Effect
# 
# def schizo_creativerter(x):
#     m = 66;
#     sd = 15;    
#     return -0.8 + 90 * skewnorm.pdf(x, -3, 70, 34)
#     
#     
# def kurtoser(val, exponent, factor=1):
#     negativitythingy = False;
#     val2 = val;
#     if(val2 < 0):
#         #print(val2)
#         negativitythingy = True;
#         val2 = -val2
#         #print(val2)
#     out = np.power(val2, exponent)
#     if(type(out) == complex):
#         out = float(out.real + out.imag)
#     if(negativitythingy == True):
#         #print("peep")
#         #print(val)
#         #print(out)
#         out = -out;
#     return ((1 - factor) * val) - factor * out ;
# 
# def too_much_kurtosing(l, exponent, factor=1):
#     nl = []
#     for i in l:
#         nl.append(kurtoser(i, exponent, factor));
#     return nl;
# 
# """
# lolz = 18 + 6 * (skewnorm.rvs(9, size=10000));
# 
# fig, ax = plt.subplots(1, 1)
# ax.hist(lolz, density=True, histtype='stepfilled', alpha=0.2)
# plt.show()
# """
# #lolz = too_much_kurtosing(pearson3.rvs(skew=0,size=100000, scale=1), 1.2, factor=0.18)
# 
# lolz = pearson3.rvs(skew=-0.6, scale=2, size=100000, loc=4.6)
# 
# x = []
# y = []
# 
# for i in range(1,130):
#     x.append(i)
#     y.append(schizo_creativerter(i))
# 
# fig, ax = plt.subplots(1, 1)
# plt.plot(x, y)
# #ax.hist(lolz, density=True, histtype='stepfilled', alpha=0.2, bins=50)
# plt.show()
# =============================================================================
