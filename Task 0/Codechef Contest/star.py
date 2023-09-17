
'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < star.py >
# Functions:        < None >
# Global variables: < None >
'''

t=int(input())                          #Test case number(t)
                                        
list=[]                                 #List to store star number
for i in range (t):                     #
    list.append(int(input()))           #Input star values for each testcase into a list
                                        
#The section below can also be used as a function
#T
                                        
for n in range (t):                     #select star value for coressponding testcase
    for a in range(list[n],0,-1):       #Decrement star value for selected testcase
        for s in range(1,a+1):          #
            if (s%5==0):                #
                print('#', end="")      #Print '#' at every 5th position
            else:                       #
                print('*', end="")      #Print '*'
        print(' ')                      #Print newline before decrement