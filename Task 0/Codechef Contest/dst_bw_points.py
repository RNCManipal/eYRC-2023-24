'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava  >
# Filename:         < dst_bw_points.py >
# Functions:        < None >
# Global variables: < None >
'''
def compute_distance(x1, y1, x2, y2):

    distance = (((x2-x1)**2)+((y2-y1)**2))**0.5

    return distance

    # Complete this function to return Euclidean distance and
    # print the distance value with precision up to 2 decimal places
'''
Purpose:
---
< calculate distance between two points with two (x,y) coordinates >

Input Arguments:
---
`< x1 >` :  [ < int > ]
    <  x coordinate of 1st point >

`< y1 >` :  [ < int > ]
    <  y coordinate of 1st point >
    
`< x2 >` :  [ < int > ]
    <  x coordinate of 2nd point >
    
`< y2 >` :  [ < int > ]
    <  y coordinate of 2nd point >

Returns:
---
`< distance >` :  [ < int > ]
    < distance between two given points >

Example call:
---
< compute_distance(a, c, b, d) >
'''


# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    for i in range(0,test_cases):
    # Write the code here to take the x1, y1, x2 and y2 values
        l1 = list(map(int, input().split()))
        x1=l1[0]
        y1=l1[1]
        x2=l1[2]
        y2=l1[3]
        
        # Once you have all 4 values, call the compute_distance function to find Euclidean distance
        print(f"Distance: {round(compute_distance(x1, y1, x2, y2),2)}")
