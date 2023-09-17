'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < if_and_for.py >
# Functions:        < main >
# Global variables: < None >
'''

# Function Name:    main (built in)
#        Inputs:    Number of test cases and integers
#       Outputs:    Numbers as output after applying conditions
#       Purpose:    Print the square of i if i is odd or double the value if i is even and if i is zero then add 3
if __name__ == '__main__':
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
      print("\r")   
