'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < if_and_for.py >
# Functions:        < None >
# Global variables: < None >
'''
if __name__ == '__main__':
    
    n = int(input("Enter n: "))
    for i in range(0,n):
        if i!=0:
            if i%2!=0:
                print(i*i)
            else:
                print(2*i)
        else:
            print(i+3)
