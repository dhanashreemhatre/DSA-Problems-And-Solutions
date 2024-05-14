t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    num1,num2=-1,-1
    if a*b>c:
        num2=b
    if a*b<c:
        num1=b
    elif a>c:
        pass
    else:
        for i in range(1,10**9+1):
            if a*i<c:
                num1=i  
                break
            elif a*i>c:
                break
            else:
                break
    print(num1,num2)