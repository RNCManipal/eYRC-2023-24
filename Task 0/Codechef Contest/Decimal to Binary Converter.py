def dec_to_binary(n):
    if n == 0:
        return '0' * 8  
    elif n == 1:
        return '0' * 7 + '1'  
    else:
        return dec_to_binary(n // 2) + str(n % 2)

# Input
T = int(input())
for _ in range(T):
    n = int(input())
    binary = dec_to_binary(n)
    print(binary.zfill(8))
