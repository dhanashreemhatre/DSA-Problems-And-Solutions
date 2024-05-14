n,dest=map(int,input().split())
trans_system=list(map(int,input().split()))
current_pos=1
for i in range(n-1):
    if (i+1)==current_pos:
        if current_pos==dest:
            break
        current_pos=current_pos+trans_system[i]
    if current_pos>dest:
        break
if current_pos!=dest:
    print("No")
else:
    print("Yes")
