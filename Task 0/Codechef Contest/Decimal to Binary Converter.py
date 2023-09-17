
'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar >
# Filename:         < Decimal to Binary Converter.py >
# Functions:        < dec_to_binary,main >
# Global variables: < None >
'''


def dec_to_binary(n):
    """
    Purpose:
    ---
    Convert a decimal number to an 8-bit binary string.

    Input Arguments:
    ---
    n : int
        The decimal number to be converted to binary.

    Returns:
    ---
    binary_str : str
        An 8-bit binary string representation of the input decimal number.

    Example:
    ---
    >>> binary = dec_to_binary(5)
    >>> print(binary)
    '00000101'
    """
    if n == 0:
        return '0' * 8
    elif n == 1:
        return '0' * 7 + '1'
    else:
        return dec_to_binary(n // 2) + str(n % 2)


# Function Name:    main (built-in)
# Inputs:           Input the Decimal number
# Outputs:          Prints the binary 8bit format of decimal number
# Purpose:          To call the  dec_to_binary() function to perform the desired conversion from decimal to binary and take the inputs in form of decimal number.
if __name__ == "__main__":
    # test_cases :Input total number of test cases
    test_cases = int(input())
    for _ in range(1,test_cases+1):
        # take the n input values
        n = int(input())
      # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
        binary = dec_to_binary(n)
        print(binary.zfill(8))
