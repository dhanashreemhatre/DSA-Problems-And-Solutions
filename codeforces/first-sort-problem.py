t=int(input())
for _ in range(t):
    num1,num2=map(int,input().split())
    if num1>num2:
        print(num2, num1)
    else:
        print(num1,num2)