'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < star.py >
# Functions:        < print_pattern,nain >
# Global variables: < None >
'''
def print_pattern(test_cases,list):
  '''
  Purpose:
  ---
  To print star pattern 
    
  Input Arguments:
  ---
  test_cases : int
    Number of star Patterns.

  list : list
    List of maximum number of stars in each pattern. 
    
  Returns:
  ---
  None
    
  Example call:
  ---
  print_pattern(test_cases,list)
  '''
  
  for n in range (test_cases):                     
    for a in range(list[n],0,-1):       #Decrement star value for selected testcase
        for s in range(1,a+1):          #
            if (s%5==0):                #
                print('#', end="")      #Print '#' at every 5th position
            else:                       #
                print('*', end="")      #Print '*'
        print(' ')                      #Print newline before decrement
  



# Function Name:    main (built in)
#        Inputs:    Number of test cases and maximum number of stars in each pattern
#       Outputs:    NONE
#       Purpose:    To call print_pattern() function and perform further operations
if __name__ == '__main__':
  test_cases=int(input())                          
  #test_cases : Number of test cases
                                        
  list=[]                                
  #list : List to store star number
  
  for i in range (test_cases):                     
    list.append(int(input()))         
  #Input star values for each testcase into a list
  print_pattern(test_cases,list)
  
  
                                        
  
