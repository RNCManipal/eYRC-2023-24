'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava >
# Filename:         < Arithamatic_Progression_with_Lamda_function.py >
# Functions:        < generate_AP,calculate_sum_of_squares,perform_operations,main >
# Global variables: < None >
'''
def generate_AP(a1, d, n):
    '''
    Purpose:
    ---
    Generates an arithmetic progression (AP) series.

    Input Arguments:
    ---
    `a1` : [int]
        The first term of the arithmetic progression.
    
    `d` : [int]
        The common difference between the terms of the arithmetic progression.
    
    `n` : [int]
        The number of terms in the arithmetic progression.

    Returns:
    ---
    `AP_series` : [list of int]
        The generated AP series.
    '''
    # a1: The initial term of the AP series
    # d: The common difference between terms
    # n: The number of terms to generate
    AP_series = [a1 + i * d for i in range(n)]
    return AP_series

def calculate_sum_of_squares(squares):
    '''
    Purpose:
    ---
    Calculates the sum of squares of a list of numbers.

    Input Arguments:
    ---
    `squares` : [list of int]
        List of numbers whose squares need to be summed.

    Returns:
    ---
    `total` : [int]
        The sum of squares of the input numbers.
    '''
    # squares: List of numbers whose squares are to be summed
    total = 0
    for square in squares:
        total += square
    return total

def perform_operations():
    '''
    Purpose:
    ---
    Performs a sequence of operations for a given number of test cases:
    1. Generate an arithmetic progression (AP) series.
    2. Print the AP series.
    3. Calculate and print the squares of its elements.
    4. Calculate and print the sum of the squares.
    '''
    t = int(input())  # Number of test cases

    for _ in range(t):
        a1, d, n = map(int, input().split())  
        AP_series = generate_AP(a1, d, n)

        print(" ".join(map(str, AP_series)))

        squares = list(map(lambda x: x ** 2, AP_series))
        print(" ".join(map(str, squares)))

        sum_of_squares = calculate_sum_of_squares(squares)
        print(sum_of_squares)




# Function Name:    main (built-in)
# Inputs:           None
# Outputs:          None
# Purpose:          To call the perform_operations() function to perform the desired operations.
if __name__ == "__main__":
    perform_operations()
