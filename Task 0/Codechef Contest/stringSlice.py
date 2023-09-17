'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava >
# Filename:         < stringSlice.py >
# Functions:        < list_slice,main >
# Global variables: < None >
'''

def list_slice(test_cases):
  '''
  Purpose:
  ---
  1.To reverse the list
  2.To add 3 to every third number in the list
  3.To substract 7 from every fifth number in the list
  4.To add  the numbers from index 3 to 7 in the list
    
  Input Arguments:
  ---
  test_cases :  int
    Total number of test cases 

  Returns:
  ---
  None

  Example call:
  ---
  list_slice(test_cases)
  '''
  while test_cases !=0:
    len1 = int((input()))

    l1 = list(map(int, input().split()))
    len1 = len(l1)
    l2 =l1[::-1]
    for item in l2:
        print(item,end=" ")
    print("\r")
    
    for i in range(0, len1, 3):
        if i == 0 :
            continue
        else:
            print(l1[i]+3,end=" ")
    print("\r")

    for i in range(0, len1, 5):
        if i == 0 :
            continue
        else:
            print(l1[i]-7,end=" ")
    print("\r")

    sum=0
    for i in range(3,8):
        sum= sum+l1[i]
    print(f"{sum}")

    test_cases= test_cases-1


# Function Name:    main (built in)
#        Inputs:    Number of test cases
#       Outputs:    None
#       Purpose:    To call the list_slice() function to perform further operations
if __name__ == '__main__':
  test_cases = int(input()) 
  #test_cases : Number of test cases

  list_slice(test_cases)
