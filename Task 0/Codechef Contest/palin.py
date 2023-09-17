'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < palin.py >
# Functions:        < None >
# Global variables: < None >
'''

num=int(input("enter the number of strings to check: "))

for i in range(0,num):
    str=input("enter string: ")
    if str == str[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
