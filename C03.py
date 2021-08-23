#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:06:12 2021

@author: kutay
"""
import math
import numpy as np

#CRR function
def CRR_stock(S_0, r, sigma, T, M):
    deltat = T / M
    alpha = math.exp(r * deltat)
    beta = 1 / 2 * (1 / alpha + alpha * math.exp(math.pow(sigma, 2) * deltat))
    u = beta + math.sqrt(math.pow(beta, 2) - 1)
    d = 1 / u
    
#empty matrix
    S = np.empty((M + 1, M + 1))
    
 #fill matrix with prices   
    for i in range(1, M + 2, 1):
        for j in range(1, i+1, 1):
            S[j-1, i-1] = S_0 * math.pow(u, j - 1) * math.pow(d, i-j)
      
            
    return S
#parameters
S_0 = 100
r = 0.05
sigma = 0.3
T = 1
M = 500

stock = CRR_stock(S_0, r, sigma, T, M)
print(stock)
            
            
    
    
    
    
    
    
