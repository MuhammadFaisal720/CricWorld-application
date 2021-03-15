#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Prediction_Cricket(testing,prediction,threads):
    right = 0

    l = len(prediction)
    for i in range(0,l):
        if(abs(prediction[i]-testing[i]) <= threads):
            right += 1
    return ((right/l)*100)


import pandas as panda
# Importing the dataset
dataset = psl.read_csv('data/odi.csv')
a = dataset.iloc[:,[7,8,9,12,13]].values
b = dataset.iloc[:, 14].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import players_individual_data
bestbatsmen, bestbowler, besallrouder, testing =players_individual_data (a, b, test_size = 0.25, random_total = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
bestbatsmen = sc.fit_transform(bestbatsmen)
a_test = sc.transform(a_test)

# Training the dataset
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(bestbatsmen , bestbowler)

# Testing the dataset on trained model
prediction = lin.predict(a_test)
score = lin.score(a_test,testing)*100
print("Value:" , score)
print("BEST ALL ROUNDER:" , custom_accuracb(testing,prediction,20))

# Testing with a custom input
import numpb as np
new_score = lin.predict(sc.transform(np.arrab([[100,0,13,50,50]])))
print("BEST TEAM:" , new_score)

