# -*- coding: utf-8 -*-
"""association-learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dfKmiX763-kpyhpa9kigW-qubLhHI9z6

Association Learning

learn --> what is support, Confidence and Life
"""

#-----------------------------------------------------------------------------------------------------------------------

import pandas as pd

dataset = pd.read_csv("Market_Basket_Optimisation.csv" , header=None)
dataset.tail()
#in our dataset label not available
#you not use header = None then machine by defult take lable of 1st row
#our dataset having some person and buy which product on mall
#see 0th person purchased many product and 2nd person only one etc.
#-----------------------------------------------------------------------------------------------------------------------

#convert our data set into list formate
transactions = []

#in our data set many type of vale available so convert into string and add transactions
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])

#-----------------------------------------------------------------------------------------------------------------------
    
# Training Apriori on the dataset
# min_length = 2 means minimum 2 data nonNaN then this data pickup
#what is support, confidence, lift see vidio lecture 
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

#-----------------------------------------------------------------------------------------------------------------------
#see our "rules" is object
print(type(rules))

#-----------------------------------------------------------------------------------------------------------------------
#convert into list
results = list(rules)

results
#see our data set having 7500 rows but in results list only 154 acoording to our rules setisfaction

#-----------------------------------------------------------------------------------------------------------------------
print(len(results))


#-----------------------------------------------------------------------------------------------------------------------
results[0]

#-----------------------------------------------------------------------------------------------------------------------

for i in range(0,len(results)):
    for j in results[i][2]:
      print('Rules:',results[i][0],'\nSupport:',results[i][1],'\nconfidence:',j[2],'\nlift:',j[3],'\n-------------------------------')
#all valuse setisfy according to our rules

#-----------------------------------------------------------------------------------------------------------------------