# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:16:47 2019

@author: Chris
"""

#import numpy as nm
#import pandas as pd
###===========================================================================
def roundup(arr):
    '''This function takes an array of either floats or ints and returns the 
        product of those elements'''
    s = 1
    for i in range(len(arr)):
        s = round(s,5) * arr[i]
    return s
###===========================================================================
def normalize(arr):
    s = 0
    for i in range(len(arr)):
        s = arr[i] + s
    for i in range(len(arr)):
        arr[i] = round(arr[i]/s,4)
    return arr
###===========================================================================
def countSubtotal(df, pos = True):
    '''This function takes:
        df - a dataframe of ints/floats with the pos/neg value in the final place
        pos - are you looking for the total number of Y's or N's in the final column?
        
        and returns:
            the count of the number of Y/N's in the final column'''
    s = 0               #Create counter variable s
    if pos == True:     #If searching for Y's
        for l in df.values:     #loop through the rows
            if (l[len(df.columns)-1] + 0) != 0: #if the diagnosis col is non-zero(indicating yes)
                s = s + 1   #iterate s
    if pos == False:        #If searching for N's
        for l in df.values:     
            if (l[len(df.columns)-1] + 0) == 0:  #if the diagnosis col is zero(indicating no)
                s = s + 1
    return s    
###===========================================================================
###===========================================================================
###===========================================================================
###===========================================================================
###===========================================================================

        
    