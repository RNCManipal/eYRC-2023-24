
def generate_AP(a1, d, n):
    AP_series = [a1 + i * d for i in range(n)]
    return AP_series

def calculate_sum_of_squares(squares):
    total = 0
    for square in squares:
        total += square
    return total

def perform_operations():
    t = int(input())  # Number of test cases

    for _ in range(t):
        a1, d, n = map(int, input().split())  
        AP_series = generate_AP(a1, d, n)

        print(" ".join(map(str, AP_series)))

        squares = list(map(lambda x: x ** 2, AP_series))
        print(" ".join(map(str, squares)))

        sum_of_squares = calculate_sum_of_squares(squares)
        print(sum_of_squares)

if __name__ == "__main__":
    perform_operations()
