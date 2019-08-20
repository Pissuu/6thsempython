print("simple calculator")
print(" enter 1 for *")
print(" enter 2 for /")
print(" enter 3 for +")
print(" enter 4 for -")
choice=int(input())
ans=int
a1=int(input("enter first argument"))
a2=int(input("enter second argument"))
if choice==1:
    ans=a1*a2
    print("answer is:",ans)  
if choice==2:
    ans=a1/a2
    print("answer is:",ans)
if choice==3:
    ans=a1+a2
    print("answer is:",ans)
if choice==4:
    ans=a1-a2
    print("answer is",ans)
    
