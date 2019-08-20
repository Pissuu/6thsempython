n=int(input("enter a number :"))
a=[0,1]
i=2
while len(a)<n:
    b=a[i-1]+a[i-2]
    a.append(b)
    i=i+1
for j in a:
    print(j)
