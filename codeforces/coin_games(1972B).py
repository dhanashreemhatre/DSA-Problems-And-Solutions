t=int(input())
for _ in range(t):
    n=int(input())
    coins_arr=list(input())
    player=['alice','bob']
    current_player=player[0]
    while coins_arr:
        if "U" not in coins_arr:
            break
        
        if "U" in coins_arr:
            index=coins_arr.index("U")
         
            if len(coins_arr)>2:
                if len(coins_arr)>index+1:
                    if coins_arr[index+1]=="U":
                        coins_arr[index+1]="D"
                    else:
                        coins_arr[index+1]="U"
                else:
                    if coins_arr[index-2]=="U":
                        coins_arr[index-2]="D"
                    else:
                        coins_arr[index-2]="U"
                if coins_arr[index-1]=="U":
                    coins_arr[index-1]="D"
                else:
                    coins_arr[index-1]="U"
            coins_arr.pop(index)
            if current_player==player[0]:
                current_player=player[1]
            else:
                current_player=player[0]
    if current_player==player[0]:
        print("No")
    else:
        print("Yes")