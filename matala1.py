# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:03:25 2023

@author: moriya
"""

# Q1.

'''This function calculate a formula with the following parameters: x1, x2, x3.'''
def calculate_func(x1,x2,x3):
    Tx1 = type(x1)
    Tx2 = type(x2)
    Tx3 = type(x3)
    if (Tx1 == int and (Tx2 == float and Tx3 == float) or Tx2 == int and (Tx1 == float and Tx3 == float) or Tx3 == int and (Tx1 == float and Tx2 == float)):
         print("Error: parameters should be float")
    elif (Tx1 != int and Tx1 != float) and (Tx2 != int and Tx2 != float) and (Tx3 != int and Tx3 != float):
        print("None")
    elif Tx1 == float and Tx2 == float and Tx3 == float:
        numerator = (x1+x2+x3)*(x2+x3)*x3
        denominator = x1+x2+x3
        if denominator == 0:
            print("Not a number - deominator equals zero")
        else:
            return float(numerator/denominator)
    else: #If not all parameters with 1 a type (that no: != int and != float)
        print("Error: parameters should be float \nNone")

# Q2.
# 2.a.

'''This function turns all letters to lowercase and reverses the word.'''
def revword (word:str) -> str:
    word = word.lower()
    return(word[::-1])     

# 2.b.      
'''This function counts the number of the first word in the file's appearances.'''
def countword() -> int:
    f = open('C:/Users/moriy/OneDrive - Ariel University/sofware/Python_mining_and_analysis/text.txt', 'r')
    file = [] # For rows
    lst = [] # For words
    for line in f: # To put the sentences in list, for to run about them.
        line = line.rstrip()
        file.append(line)
        
    for r in file: # For row in file
        if r is file[0]:
            word = r
            lst.append(word)
        else:
            r = r.split()
            for w in r: # For word in row
                fixWord = revword(w)
                lst.append(fixWord)
    counter = 0
    for i in lst:
        if i == word:
            counter += 1
    return(counter)
