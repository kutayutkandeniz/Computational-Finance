#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:03:58 2021

@author: kutay
"""
#import neccesary libraries
import math
import numpy as np
import matplotlib.pyplot as plt

#set parameters
mean = 0.0002
std_dev = 0.001
starting_value = 10


#create sample of 500 with given std dev and mean
random_vector = np.random.normal(mean, std_dev, 500)


#function parameter x
def simulate(x):
#save the length of array in n
    n = len(x)
#create an array of zeros to save stock prices    
    result = np.zeros(n)
#save start value in the first element of array    
    result[0] = starting_value
    
    
#calulates the i-th stock price depending on the (i-1)-th stok price and the (i-1)-th log return    
    for i in range(1,n):
        result[i] = math.exp(x[i-1]) * result[i-1]
    return result
#test
sim = simulate(random_vector)
#plot
plt.plot(sim)
plt.show()