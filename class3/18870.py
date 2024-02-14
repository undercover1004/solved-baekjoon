N = int(input())

arr = list(map(int, input().split()))

list_arr = sorted(list(set(arr)))

dict = {}
for i in range(len(list_arr)):
    dict[list_arr[i]] = i

for num in arr:
    print(dict[num], end=' ')