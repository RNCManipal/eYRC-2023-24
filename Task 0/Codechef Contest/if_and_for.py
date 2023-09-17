'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < if_and_for.py >
# Functions:        < None >
# Global variables: < None >
'''
test_cases = int(input())

for i in range(0,test_cases):
    n = int(input())
    for i in range(0,n):
            if i!=0:
                if i%2!=0:
                    print(i*i,end=" ")
                else:
                    print(2*i,end=" ")
            else:
                print(i+3,end=" ") 
    print("\n")   
