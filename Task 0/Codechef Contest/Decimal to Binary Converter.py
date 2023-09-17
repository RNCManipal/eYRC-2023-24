

'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava >
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

    bin_num = bin(n)[2:]
    bin_num = bin_num.zfill(8)
    return bin_num

# Function Name:    main (built-in)
# Inputs:           Input the Decimal number
# Outputs:          Prints the binary 8bit format of decimal number
# Purpose:          To call the  dec_to_binary() function to perform the desired conversion from decimal to binary and take the inputs in form of decimal number.
if __name__ == '__main__':
    # take the T (test_cases) input
    test_cases = int(input())
    list=[]*25

    # Write the code here to take the n value
    for case in range(test_cases):
        # take the n input values
        n = int(input())
        list.append(n)

        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
    for a in range( test_cases ):
        bin_num = dec_to_binary(list[a])
        print(bin_num)
