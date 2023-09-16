test_cases=int(input("no of test cases: "))
l1=[]
for j in range(0,test_cases):
    str = input("enter a string: ")
    l1.append(str)


def count_letters(str):
    lst=str.split()
    for i in range(0,len(lst)):
        if i==0:
            print(len(lst[i])-1,end=",")
        elif i == len(lst)-1:
            print(len(lst[i]))
        else:
            print(len(lst[i]),end=",")

for item in l1:
    count_letters(item)