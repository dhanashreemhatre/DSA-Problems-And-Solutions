t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    a1=min(a,b)
    b1=max(a,b)
    if (c>=a1 and  c<=b1) and (d>=a1 and d<=b1):
        print("No")
    elif (c>=a1 and  c<=b1) or (d>=a1 and d<=b1):
        print("Yes")
    else:
        print("No")