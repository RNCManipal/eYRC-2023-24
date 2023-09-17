'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < dst_bw_points.py >
# Functions:        < compute_distance >
# Global variables: < None >
'''

def compute_distance(x1, y1, x2, y2):

    distance = (((x2-x1)**2)+((y2-y1)**2))**0.5

    return distance

    '''
Purpose:
---
< To Calculate the distance between given twopoints(x,y coordinate) >

Input Arguments:
---
`< x1 >` :  [ < int > ]
    < x coordinate of 1st point >

`< y1 >` :  [ < int > ]
    < y coordinate of 1st point >

`< x2 >` :  [ < int > ]
    < x coordinate of 2nd point >

`< y2 >` :  [ < int > ]
    < y coordinate of 2nd point >

Returns:
---
`< distance >` :  [ < int > ]
    < returns the distace between given points >

Example call:
---
< compute_distance(a,b ,A ,B ) >
'''



# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    for i in range(0,test_cases):
    # Write the code here to take the x1, y1, x2 and y2 values
        x1 = int(input("enter x1: "))
        x2 = int(input("enter x2: "))
        y1 = int(input("enter y1: "))
        y2 = int(input("enter y2: "))
        
        # Once you have all 4 values, call the compute_distance function to find Euclidean distance
        print(round(compute_distance(x1, y1, x2, y2),2))
        
