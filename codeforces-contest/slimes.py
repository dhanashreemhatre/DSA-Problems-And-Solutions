t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    result = [-1] * n
    stack = []

    # Iterate from left to right to find the nearest greater slime on the left
    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            result[i] = max(result[i], i - stack[-1])
            stack.pop()
        stack.append(i)

    # Clear the stack for the next iteration
    stack = []

    # Iterate from right to left to find the nearest greater slime on the right
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] < a[i]:
            result[i] = max(result[i], stack[-1] - i)
            stack.pop()
        stack.append(i)

    # If there is a greater slime on both sides, calculate the gap between them as time
    for i in range(n):
        if result[i] != -1 and result[i] < i:
            result[i] = i - result[i]

    print(*result)
