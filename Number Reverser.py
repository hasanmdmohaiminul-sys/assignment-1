num=int(input("enter number:"))
rnum=0
while num>0:
    lastdigit=num%10
    rnum=rnum*10+lastdigit
    num=num//10
print(rnum)