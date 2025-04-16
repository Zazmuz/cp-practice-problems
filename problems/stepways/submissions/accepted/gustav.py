n = int(input())
a = 1
b = 1
for i in range(n):
    c = (a+b)%1000000007
    a,b = b,c
print(a)