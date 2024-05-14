t = int(input())

for _ in range(t):

    s=input()
    slices=1
    changed=s[0]
    found=0
    for index,char in enumerate(s):
        if index==0 and char=='0':
            if changed==char:
                pass
            else:
                changed=char
                slices+=1
        else:
            if changed=='0':
                if changed==char:
                    found=1
                    pass
                else:
                    changed=char
            else:
                if changed==char:
                    pass
                else:
                    changed=char
                    slices+=1
    if len(s)>3:
        count=s.count('01')
        if count>1:
            slices+=count-1
    print(slices)