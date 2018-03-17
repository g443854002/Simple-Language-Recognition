# Simple-Language-Recognition
Name: Carl Xu


This is the read me file for my assignment two regarding letter bigram and word bigram with two smoothing methods. (Add one, good turing) There are four parts in the file. They are Q1(question1), Q2(question2), Analysis and Q3(extra credit). For each question, there are two parts in it, brief summary and instruction. Brief summary give some ideas about the program and intuition behind it. And it also includes some thoughts. Instruction part provides step by step instruction how does the program works and what files are needed before you run the program.

Q1:
Brief summary:
The accuracy rate is 93.0 % for my letter bigram program, and it takes 11.6 seconds to run the program. I used the sample bigram code provided to create the nested bigram dictionary. And I calculate the probability for each bigram, and replace the number of occurrence with my probability rate. And I create and bigram list from input test file. And I used dictionary key match method to search whether the bigram for test file is in the trained models. I use log probability because I want to avoid numerical underflow. And log(0) is nothing but cause math domain error. I decided to remove those unseen bigrams. 

Instruction:
The code for question 1 is stored in “letterLangId.py”, Python 3 or above is preferred.
	
First, you should have LangId.train.English, LangId.train.Italian, LangId.train.French, dicts.py ready in the same directory (Those training sets should have the same Unicode with your computer)

Scroll down to the end, there is a function called ‘get_test_result’, put the text file you want to test in this function. It will generate output file called ‘letterLangId.out’.

After that, you can see the output file in your directory. You can also calculate the accuracy by putting the solution file and ‘letterLangId.out’ into ‘get_accuracy’ function. It will output a file called ‘question1_acc.txt’, there is accuracy rate and run time for this program. 


Q2:

Brief summary:
The accuracy rate is 100.0 % for my word bigram with add one smoothing. I used the formula provided in the class to create a new algorithm to calculate the sentence probability. The functions and procedure are basically the same as question 1. But I have some new functions that calculate the type, tokens and occurrence of the first word in bigram. Those are necessary for me to create my add one smoothing algorithm. According to the result I get, it surprised me. It is a big move from the question 1.  

Instruction:
The code for question 1 is stored in “wordLangId.py”, Python 3 or above is preferred.
	
First, you should have LangId.train.English, LangId.train.Italian, LangId.train.French, dicts.py ready in the same directory (Those training sets should have the same Unicode with your computer)

Scroll down to the end, there is a function called ‘get_result’, put the text file you want to test in this function. It will generate output file called ‘wordLangId.out’.

After that, you can see the output file in your directory. You can also calculate the accuracy by putting the solution file and ‘wordLangId.out’ into ‘get_accuracy’ function. It will output a file called ‘question2_acc.txt’, there is accuracy rate and run time for this program. 


Analysis

Base on the result I have, I prefer the word bigram model with add one smoothing since it have the highest accuracy rate. For the letter bigram, I think I apply some kind of smoothing here, because I remove all 0-occurrence bigram. I only calculate the summation of log probability of existing bigrams. I think I lost some information while I am removing those unseen bigrams. But I believe there is some advantage of the letter bigram model in the first question, that is, for an Italian sentences, when I apply English model on it. Most of bigram in this Italian sentences is being removed because there are too many unseen bigrams, which result in high possibility classify this sentence to Italian. Add one smoothing take 0-occurrence bigrams into account. We can have more evident to tell what language is for certain sentence. Also, add one smoothing is easy to implement in the program. But add one smoothing still have some drawbacks, it put too much weight on some unseen bigrams. Some time, we may not want those unseen bigram take too much portion of total probability.

Extra Credit

Q3
Brief summary:

The accuracy rate is 99.67 % for my word bigram with Good Turing Smoothing. The whole idea for good turing smoothing is reestimate probability mass assigned to N-grams with zero counts. Most of part in this program is basically the same as the question2. But I changed the smoothing algorithm. I applied the formula and idea from the class into this program. We have Ni and Ni+1 in the formula. I set (i = 5) So it covers most of number of Ni in the bigrams. And it is also easier to calculate. The result turns out to be good. I would prefer good turing model among these three models because couple of reasons. First, good turing method is based on binomial distribution assumption. It creates classes Nc of N-grams that occur c times. It reallocate the probability mass of bigrams that we seen once to bigram that never seen. It does not have the drawbacks that add one smoothing have. It does not put too much weight on unseen bigrams. Eventhough, it did not reach the 100%, but it works perfectly.


Instruction:
The code for question 1 is stored in “wordLangId2.py”, Python 3 or above is preferred.
	
First, you should have LangId.train.English, LangId.train.Italian, LangId.train.French, dicts.py ready in the same directory (Those training sets should have the same Unicode with your computer)

Scroll down to the end, there is a function called ‘get_final_result’, put the text file you want to test in this function. It will generate output file called ‘wordLangId2.out’.

After that, you can see the output file in your directory. You can also calculate the accuracy by putting the solution file and ‘wordLangId2.out’ into ‘get_accuracy’ function. It will output a file called ‘question3_acc.txt’, there is accuracy rate and run time for this program. 



