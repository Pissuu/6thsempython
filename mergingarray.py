n1=int(input("enter the number of elements in first array:"))
i=0
a=[]
while i<n1:
    print("enter",i+1,"element")
    b=input()
    a.append(b)
    i=i+1
print(a)
n2=int(input("enter the number of elements in second array:"))
i=0
a=[]
while i<n2:
    print("enter",i+1,"element")
    b=input()
    a.append(b)
    i=i+1
print(b)
for i in b:
    while i not in a:
        a.append(i)
print("after appending",a)
