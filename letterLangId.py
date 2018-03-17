#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:28:10 2018

@author: Carl Xu, yuehaox2
"""
# Letter bigram language recognition program

# Import package
from dicts import DefaultDict
import math
import sys
import timeit

start = timeit.default_timer()
# Function that create bigrams from text
def bigrams(words):
    d = DefaultDict(DefaultDict(0))
    for (w1, w2) in zip([None] + words, words + [None]):
        d[w1][w2] += 1
    return d

def file2bigrams(filename):
    letter = [list(words) for words in open(filename).read()]
    f = [i[0] for i in letter]
    return bigrams(f)

# Create probability base on the value in bigram dictionary
def getprob(dictionary):
    for k1,v1 in dictionary.items():
        counts = v1.values()
        total = sum(counts)
        v1.update((k2,round(v2/total,16)) for k2,v2 in v1.items())
    return(dictionary)
    


# English model 
def Eng_prob(bigram):   
    log_prob = 0
    for j in range(len(bigram)):
        first = bigram[j][0]
        second = bigram[j][1]
        for k1,v1 in english_mod.items():
            if first in english_mod and second in v1:
                p = english_mod.get(first).get(second)
                if(isinstance(p, float)):
                    log_prob += math.log(english_mod.get(first).get(second))
    return(log_prob)

# Italian model
def Ita_prob(bigram):   
    log_prob = 0
    for j in range(len(bigram)):
        first = bigram[j][0]
        second = bigram[j][1]
        for k1,v1 in italian_mod.items():
            if first in italian_mod and second in v1:
                p = italian_mod.get(first).get(second)
                if(isinstance(p, float)):
                    log_prob += math.log(italian_mod.get(first).get(second))
    return(log_prob) 
 
# French model               
def Fre_prob(bigram):   
    log_prob = 0 
    for j in range(len(bigram)):
        first = bigram[j][0]
        second = bigram[j][1]
        for k1,v1 in french_mod.items():
            if first in french_mod and second in v1:
                p = french_mod.get(first).get(second)
                if(isinstance(p, float)):
                    log_prob += math.log(french_mod.get(first).get(second))
    return(log_prob) 
  
# Create a list of result from the models and input text file
def get_test_result(file):
    n = 1 
    new = []
    orig_stdout = sys.stdout
    sys.stdout = open('letterLangId.out','wt')
    with open(file) as f:
        line = f.readlines()
    for m in line:    
        bigram = [m[i:i+2] for i in range(len(m)-1)]
        prob_eng = Eng_prob(bigram)
        prob_fren = Fre_prob(bigram)
        prob_ita = Ita_prob(bigram)
        best = max(prob_eng, prob_fren, prob_ita)
        if prob_eng == best:
            new.append(str(n)+' '+'English')
        elif prob_ita == best:
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
    acc = len(inter)/len(content1)*100
    
    sys.stdout = open('question1_acc.txt','wt')
    print('The accuracy rate is '+str(acc)+' %')
    
# Language probability models   
english_mod = getprob(file2bigrams('LangId.train.English'))

italian_mod = getprob(file2bigrams('LangId.train.Italian'))

french_mod = getprob(file2bigrams('LangId.train.French')) 
# Put your text file in 'get_test_result' function
# It will create a 'letterLangId.out' file in your directory
get_test_result('LangId.test')

# Put your solution file. It will create a accuracy text file
# called 'question1_acc.txt'

get_accuracy('LangId.sol', 'letterLangId.out')

# Calculate the time
stop = timeit.default_timer()

print('It takes '+ str(stop-start) + ' second')