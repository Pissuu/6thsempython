import random
import string
st=input("enter the string to compare against")
n=len(st)
number=0
def randomString(stringLength=n):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
while randomString()!=st:
    print(randomString())
    number+=1
print(number)
    
