N = int(input())
dp = [[0] * 3 for _ in range(2)]
Max = [0, 0, 0]
Min = [0, 0, 0]
arr = []

for i in range(N):
    arr = list(map(int, input().split()))
    # dp[0] => max 저장
    dp[0][0] = max(Max[0], Max[1]) + arr[0]
    dp[0][1] = max(Max[0], Max[1], Max[2]) + arr[1]
    dp[0][2] = max(Max[1], Max[2]) + arr[2]

    # dp[1] => min 저장
    dp[1][0] = min(Min[0], Min[1]) + arr[0]
    dp[1][1] = min(Min[0], Min[1], Min[2]) + arr[1]
    dp[1][2] = min(Min[1], Min[2]) + arr[2]

    for j in range(3):
        Max[j] = dp[0][j]
        Min[j] = dp[1][j]

print(max(Max[0], Max[1], Max[2]), min(Min[0], Min[1], Min[2]), sep=" ")