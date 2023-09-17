'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < countChars.py >
# Functions:        < count_letters >
# Global variables: < None >
'''

test_cases=int(input())
l1=[]
for j in range(0,test_cases):
    str = input()
    l1.append(str)


def count_letters(str):
    '''
Purpose:
---
< count letters of each word in a line begining  with '@' >

Input Arguments:
---
`< str >` :  [ < string > ]
    < A line string  >

Returns:
---
`< None >` :  [ < None > ]
    < None >

Example call:
---
< count_letters(line) >
'''

    
    lst=str.split()
    for i in range(0,len(lst)):
        if i==0:
            print(len(lst[i])-1,end=",")
        elif i == len(lst)-1:
            print(len(lst[i]))
        else:
            print(len(lst[i]),end=",")

for item in l1:
    count_letters(item)
