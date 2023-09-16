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