#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:04:10 2020

@author: david
"""
import pandas as pd 
import re 

number = re.compile('\d+')    #creates a object that matches numbers
defitiency =[]  #creates a lists where the digit matches can be storted


data = pd.read_csv('deficiencia_items.csv') #reads the csv file
df = pd.DataFrame(data) #converts it into a pandas df

#print(df['Deficiencia'].values)
#print(df['items'].values)

for i in df['items'].values:        #gets the values of the columm 'items'
                                    #which are a series of strings in a list 
                                    #that look like this: ['0, 9, 10, 4', ... ,'12 ,13']
                                    
    defitiency.append(number.findall(i))  #finds all the digits and appends the match to 
                                        #defitiency

def toInt(x):
    
    new=[]  #list where the converted to int elements of the subsets are stored 
    final=[] #list where the subsets converted to int are storted
    
    for Set in x:               #access the lists in the list
        
        for element in Set:     #access the elements in the list
            new.append(int(element))    #appends the converted element to the list
                        
        final.append(new)       #appends the converted new lists to the final list
        new=[]                  #resets new in order to be able to store the other lists
        
    return final                #gives the converted list of lists 





defitiency = toInt(defitiency)  #list of strings is converted to list of lists of integers
#print(defitiency)

df = pd.DataFrame(list(zip(df['Deficiencia'].values, defitiency)), columns= ['defitiency','buttons']) #actualices the data frame
                              #with the values of the new defitiency list and the same labels
#print(df)
                              
