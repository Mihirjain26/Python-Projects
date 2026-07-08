import random
length=int(input("enter the length of password : "))

result=""

def password(b,result):
    result=result+b
    return result


for i in range(0,length,1):
    choice=random.randint(1,4)
    match choice:
        case 1:
            a1=random.randint(48,57)
            b1=chr(a1)
            result=password(b1,result)
        case 2:
            a2=random.randint(65,90)
            b2=chr(a2)
            result=password(b2,result)
        case 3:
            a3=random.randint(97,122)
            b3=chr(a3)
            result=password(b3,result)
        case 4:
            a4=random.randint(33,47)
            b4=chr(a4)
            result=password(b4,result)

print(result)