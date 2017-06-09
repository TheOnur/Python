def linear_search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

arr =[1, 3, 4, 5, 6, 8, 5]
x = 5
res = linear_search(arr, x)
if res != -1:
    print('Item found at : ' + str(res + 1))
else:
    print('Item not found')