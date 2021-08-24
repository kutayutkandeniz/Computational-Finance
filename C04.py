#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:05:19 2021

@author: kutay
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#(1)

def log_returns(data):
    
#applies log to each element of data and  take diff, returns x2-x1,x3-x2....   
    return np.diff(np.log(data))


#(2)

#since from csv file import and format
dax = np.genfromtxt('time_series_dax_2021.csv', delimiter=';', usecols=4, skip_header=1)
#data is starting from the most recent so we flip it and it start from oldeest
dax = np.flip(dax)

#applying log return funtion to dax data
lr = log_returns(dax)



#to annalize mean and std dev we multiply with 250
ev = np.mean(lr)
std_dev = math.sqrt(np.var(lr))
print('annuealized mean = ' + str(ev *250) + 'annualieed std dev = ' + str(std_dev*math.sqrt(250)) + '.'   )

 
#(3)
lr_simulated = np.random.normal(ev, std_dev, len(lr))


plt.clf()
plt.plot(lr,'b')
plt.plot(lr_simulated, 'r')
plt.title('log-returns of DAX in the period 14/04/1998-14/04/2020')
plt.xlabel('trading day')
plt.ylabel('log-returns')

plt.show()

#blue ones are the real log retunrns and red nes are the simulateed ones. since 
#normal distribution is not suitable for simulateing lof returns there are lots of spike differences
