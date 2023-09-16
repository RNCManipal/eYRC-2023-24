l1 = []

len = int(input("Length of list: "))
for i in range(0,len):
    a=int(input("Enter number: "))
    l1.append(a)

print(l1[::-1])

print((l1[::2])+3)

print((l1[::5])-7)

for i in range(3,8):
    sum+=l1[i]
print(sum)
