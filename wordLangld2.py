#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:46:44 2018

@author: Carl Xu, yuehaox2
"""

from dicts import DefaultDict
import sys
import math
import timeit

start = timeit.default_timer()
# Word bigram language recognition program with good turing smoothing

# Create a bigram nested dictionary
def bigrams(words):
    d = DefaultDict(DefaultDict(0))
    for (w1, w2) in zip([None] + words, words + [None]):
        d[w1][w2] += 1
    return d

def file2bigrams(filename):
    return bigrams(open(filename).read().split())

# Get total number of bigrams (token)
def get_N(dictionary):
    n = 0
    for k1,v1 in dictionary.items():
        n += (sum(v1.values()))
    return (n)

# Get Ni up to N6
# So we can redistribute the new counts up to N5
def get_Ni(dictionary):
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    for k1,v1 in dictionary.items():
        for k in v1.values():
            if k == 1:
                n1 +=1
            if k == 2:
                n2 +=1
            if k == 3:
                n3 +=1
            if k == 4:
                n4 +=1
            if k == 5:
                n5 +=1
            if k == 6:
                n6 +=1
    n = [n1,n2,n3,n4,n5,n6]
    return(n)

# Base on the good turing formulate calculate the probability 
# for 0 occurence bigrams and redistributed words in N1-N5.    
def get_prob(bigram,dictionary,ni,n):
    n1 = ni[0]
    n2 = ni[1]
    n3 = ni[2]
    n4 = ni[3]
    n5 = ni[4]
    n6 = ni[5]  
    first = bigram[0]
    second = bigram[1]
    p = 0
    if first not in dictionary:
        p = math.log(n1/n)
    if first in dictionary:
        if second in dictionary.get(first).values():
            if dictionary.get(first).values() == 1:
                new_count = (2*n2)/n1
                p = math.log(new_count/n)
            elif dictionary.get(first).values() == 2:
                new_count = (3*n3)/n2
                p = math.log(new_count/n)
            elif dictionary.get(first).values() == 3:
                new_count = (4*n4)/n3
                p = math.log(new_count/n)
            elif dictionary.get(first).values() == 4:
                new_count = (5*n5)/n4
                p = math.log(new_count/n)
            elif dictionary.get(first).values() == 5:
                new_count = (6*n6)/n5
                p = math.log(new_count/n)
            else:
                p = math.log(dictionary.get(first).values()/n)
                
    return(p)

# Calculate the final sentences probability 
def get_result(bigram,dictionary):
    n = get_N(dictionary)
    ni = get_Ni(dictionary)
    log_total = 0
    for i in range (len(bigram)):
        prob =  get_prob(bigram[i],dictionary,ni,n)
        if(isinstance(prob, float)):
            log_total += prob
    return(log_total) 
    
# Make prediction based on the calculated probability. And output the result
def get_final_result(text):
    n = 1
    new = []
    orig_stdout = sys.stdout
    sys.stdout = open('wordLangId2.out','wt')
    with open(text) as f:
        mylist = f.read().splitlines()
    for i in range(len(mylist)):
        tokens = mylist[i].split(" ")
        bigrams = ([(tokens[i], tokens[i+1]) for i in range(0, len(tokens)-1)])
        eng = get_result(bigrams,eng_dic) 
        ita = get_result(bigrams,ita_dic)
        fre = get_result(bigrams,fre_dic)
        best = max(eng,ita,fre)
        if eng == best:
            new.append(str(n)+' '+'English')
        elif ita == best:
            new.append(str(n)+' '+'Italian')
        else:
            new.append(str(n)+' '+'French')
        n = n + 1
    for i in range(len(new)):
       print(new[i]) 
    sys.stdout.close()
    sys.stdout = orig_stdout
    
# Compare accuracy rate between result and solution   
def get_accuracy(text,mine):
    with open(text) as f1:
        content1 = f1.read().splitlines()
    with open(mine) as f2:
        content2 = f2.read().splitlines()             
    inter = list(set(content1) & set(content2))
    acc = (len(inter)/len(content1))*100
    sys.stdout = open('question3_acc.txt','wt')
    print('The accuracy rate is '+str(acc)+' %')
    
# Language models    
eng_dic = (file2bigrams('LangId.train.English'))
ita_dic = (file2bigrams('LangId.train.Italian'))
fre_dic = (file2bigrams('LangId.train.French'))       
 
# Put your text file in 'get_final_result' function
# It will create a 'wordLangId2.out' file in your directory
get_final_result('LangId.test')

# Put your solution file. It will create a accuracy text file
# called 'question3_acc.txt'
get_accuracy('LangId.sol','wordLangId2.out')

    
# Calculate the time
stop = timeit.default_timer()

print('It takes '+ str(stop-start) + ' second')
        
        
        
        
        
        