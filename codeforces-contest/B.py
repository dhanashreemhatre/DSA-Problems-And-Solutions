def is_good_subarray(c, l, r):
    # Calculate the sum of the subarray [l, r]
    subarray_sum = sum(c[l-1:r])
    
    if subarray_sum%2 == 0 :
        return "No"
    else:
        return "Yes"

t = int(input())  # Number of test cases
for _ in range(t):
    n, q = map(int, input().split())  # Length of array and number of queries
    c = list(map(int, input().split()))  # The array c
    for _ in range(q):
        l, r = map(int, input().split())
        print(is_good_subarray(c, l, r))
