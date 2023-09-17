'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < palin.py >
# Functions:        < main >
# Global variables: < None >
'''

# Function Name:    main (built in)
#        Inputs:    Number of test cases and strings
#       Outputs:    To print string is Palindrome or not Palindrome
#       Purpose:    To check Strig is Palindrome or not Palindrome
if __name__ == '__main__':
  t=int(input())
  
  for i in range(t):
    str=input()
    if str.capitalize() == str[::-1].capitalize():
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
