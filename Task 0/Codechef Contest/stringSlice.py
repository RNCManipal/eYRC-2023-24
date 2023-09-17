'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < stringSlice.py >
# Functions:        < None >
# Global variables: < None >
'''

test_cases = int(input())

while test_cases !=0:
    len1 = int((input()))

    l1 = list(map(int, input().split()))
    len1 = len(l1)
    l2 =l1[::-1]
    for item in l2:
        print(item,end=" ")

    print("\n")
    for i in range(0, len1, 3):
        if i == 0 :
            continue
        else:
            print(l1[i]+3,end=" ")
    print("\n")
   

    for i in range(0, len1, 5):
        if i == 0 :
            continue
        else:
            print(l1[i]-7,end=" ")
    print("\n")

    sum=0
    for i in range(3,8):
        sum= sum+l1[i]
    print(f"{sum}")

    test_cases= test_cases-1
