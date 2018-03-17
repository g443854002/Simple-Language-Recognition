#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:54:26 2018

@author: Carl Xu, yuehaox2
"""

from dicts import DefaultDict
import sys
import math
import timeit

start = timeit.default_timer()
# Word bigram language recognition program with add one smoothing

# Create a bigram nested dictionary
def bigrams(words):
    d = DefaultDict(DefaultDict(0))
    for (w1, w2) in zip([None] + words, words + [None]):
        d[w1][w2] += 1
    return d

def file2bigrams(filename):
    return bigrams(open(filename).read().split())

# Get total number of bigrams (token)
def get_c(dictionary):
    c = 0
    for k1,v1 in dictionary.items():
        c += (sum(v1.values()))
    return (c)

# Get unique number of bigrams (type)   
def get_v(dictionary):
    v = 0
    for k1,v1 in dictionary.items():
        for k2,v2 in v1.items():
            v += 1
    return (v)

# Get the number of first word in bigrams
def get_first(dictionary,word):
    if word not in dictionary:
        return 1
    
    counts = sum(dictionary[word].values())
    return(counts)          
        

# Calculate sentences probability in three condiction.

# First, all words in bigrams are in the trained models. We just apply
# add one smoothing on it.
    
# Second, if first word in the dictionary and second word not in the
# nested dictionary. We apply different formula to calculate the probility
    
# Third, if the bigram in the text with occurences 0, we use 1 over type
# to calculate the probility
def get_sen_prob(dic,bigrams,v):
    first = bigrams[0]
    second = bigrams[1]
    if first in dic:
        if second in dic.values():
            total = dic.get(first).get(second)
            ini = get_first(dic,first)
            prob = math.log((total + 1)/(ini + v))
        if second not in dic.values():
            ini = get_first(dic,first)
            prob = math.log(ini/(ini+v))
    else:
        prob = math.log(1/v)
    return (prob)

# Calculate the final sentences probability
def fianl_prob (dic,ini,bigrams):
    c = get_c(dic)
    v = get_v(dic)
    log_total = math.log(((get_first(dic,ini))+1)/(c+v))  
    for j in range (len(bigrams)):
        log_prob =  get_sen_prob(dic, bigrams[j], v)
        if(isinstance(log_prob, float)):
            log_total += log_prob
    return (log_total)

# Make prediction on sentences language and compare to the solution
def get_result(text):
    n = 1
    new = []
    orig_stdout = sys.stdout
    sys.stdout = open('wordLangId.out','wt')
    with open(text) as f:
        mylist = f.read().splitlines()
    for i in range(len(mylist)):
        tokens = mylist[i].split(" ")
        bigram = ([(tokens[i], tokens[i+1]) for i in range(0, len(tokens)-1)])
        eng = fianl_prob(eng_dic,tokens[0],bigram) 
        ita = fianl_prob(ita_dic,tokens[0],bigram)
        fre = fianl_prob(fre_dic,tokens[0],bigram)
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
    sys.stdout = open('question2_acc.txt','wt')
    print('The accuracy rate is '+str(acc)+' %')
    
# Language probability models    
eng_dic = (file2bigrams('LangId.train.English'))
ita_dic = (file2bigrams('LangId.train.Italian'))
fre_dic = (file2bigrams('LangId.train.French'))

# Put your text file in 'get_result' function
# It will create a 'wordLangId.out' file in your directory

get_result('LangId.test')

# Put your solution file. It will create a accuracy text file
# called 'question2_acc.txt'
get_accuracy('LangId.sol','wordLangId.out')

# Calculate the time
stop = timeit.default_timer()

print('It takes '+ str(stop-start) + ' second')