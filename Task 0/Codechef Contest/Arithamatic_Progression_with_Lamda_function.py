# Function to generate the Arithmetic Progression (A.P.) series
def generate_AP(a1, d, n):
    AP_series = [a1 + i * d for i in range(n)]
    return AP_series

# Function to calculate the sum of squares without using functools.reduce
def calculate_sum_of_squares(squares):
    total = 0
    for square in squares:
        total += square
    return total

# Main function to perform operations on the A.P. series
def perform_operations():
    t = int(input())  # Number of test cases

    for _ in range(t):
        a1, d, n = map(int, input().split())  # First term, common difference, and number of terms
        AP_series = generate_AP(a1, d, n)

        # Print the A.P. series
        print(" ".join(map(str, AP_series)))

        # Calculate the squares of terms in the series
        squares = list(map(lambda x: x ** 2, AP_series))
        print(" ".join(map(str, squares)))

        # Compute the sum of the squares of terms in the series without using reduce
        sum_of_squares = calculate_sum_of_squares(squares)
        print(sum_of_squares)

# Run the program
if __name__ == "__main__":
    perform_operations()
