import numpy as np
import pandas as pd
import math as math

def countSubtotal(df, pos = True):
    '''This function takes:
        df - a dataframe of ints/floats with the pos/neg value in the final place
        pos - are you looking for the total number of Y's or N's in the final column?
        
        and returns:
            the count of the number of Y/N's in the final column'''
    s = 0               #Create counter variable s
    if pos == True:     #If searching for Y's
        for l in df.values:     #loop through the rows
            if (l[len(df1.columns)-1] + 0) != 0: #if the diagnosis col is non-zero(indicating yes)
                s = s + 1   #iterate s
    if pos == False:        #If searching for N's
        for l in df.values:     
            if (l[len(df1.columns)-1] + 0) == 0:  #if the diagnosis col is zero(indicating no)
                s = s + 1
    return s

def prob(t,data,yCount, example, pos):
    ''' t = list/tuple of column titles in sample set
        data = dataframe of samples
        YCount = number of Y's in sample set
        example = list/tuple of sample characteristics to test
        pos = True to calculate probability of subject being positive(default), 
              False for probability of negative
    '''
    if pos == False:        #If looking for N's:
        Probs = [0] * len(t)    #Instantiates result vector
        for j in range(len(t) - 1): #loop thru the columns exept for the last
            for i in data.values:   #Loop through the rows
                if (((i[j]+0) == example[j]) and ((i[len(t)-1]+0) == 0)): #For every row where the value in this column matches the sample's
                    Probs[j] = Probs[j] + 1 #Iterate the count for this one
            Probs[j] = Probs[j]/yCount #Convert counts to probabilities
    if pos == True: #If looking for N's
        Probs = [0] * len(t)    #Instantiate results vector
        for j in range(len(t) - 1): #Loop thru
            for i in data.values:   #Roll thru columns
                if (((i[j]+0) == example[j]) and ((i[len(t)-1]+0) != 0)): #If...
                    Probs[j] = Probs[j] + 1 # Iterate counter
            Probs[j] = Probs[j]/yCount #convert counts to probabilities
    
    Probs[len(t)-1] = yCount/len(data.values) #Populate final space in result vector
    return Probs #Return probability vector
############################################################################
def roundup(arr):
    '''This function takes an array of either floats or ints and returns the 
        product of those elements'''
    s = 1
    for i in range(len(arr)):
        s = round(s,5) * arr[i]
    return s


filename = 'sample.csv' # Examples test file
df1 = pd.read_csv(filename)  # Read examples into a dataframe called 'df'
ex = [1,0,1]


titles = list(df1.columns.values)  # create a tuple of the column headers of df
Ysum = countSubtotal(df1,True)  #Counts total number of positive cases from last column in datafram
Nsum = countSubtotal(df1,False)  #Counts total # of negative cases

yPr = prob(titles,df1,Ysum,ex,False)    # Returns array of conditional probabilities of length (# of features), assuming positive for final diagnosis
nPr = prob(titles,df1,Nsum,ex, False)   # Returns array of cond. probs assuming neg
yProb = roundup(yPr)    #Generates final probability of positive diagnosis with sample feature set
nProb = roundup(nPr)        #generates final prob of neg. diagnosis
# print(yPr,yProb,'\n',nPr,nProb)
print("There is a", (yProb*100), "% chance that the sample is positive for the flu.")
print("There is a", round(nProb*100, 2), "% chance that the sample is negative for the flu.")
