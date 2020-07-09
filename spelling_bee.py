# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:07:14 2020
@author: James Cotter
"""

#import dictionary
from nltk.corpus import words
word_list = words.words()

#set letters
letters = 'lticvo' #outside letters
middle = 'r' #letter that must be used

#solution with possible duplicates
sol = [w for w in word_list if set(w).difference(set(letters)) == set(middle) and 5<=len(w)]

#solution without duplicates
solution = []
[solution.append(x) for x in sol if x not in solution]

#find and print words that use every letter
all_letters = [x for x in solution if set(x) == set(letters).union(set(middle))]
for i in all_letters:
    print(i)

#calculate and print final total score
total_score = 3*len(all_letters) + len(solution)-len(all_letters)
print("Total score is: ", total_score)