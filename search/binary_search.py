def binary_search(arr, left, right, x):
    if left <= right:
        middle = left + (right -left) // 2
        if arr[middle] == x:
            return middle
        elif arr[middle] < x:
            return binary_search(arr, middle + 1, right, x)
        else:
            return binary_search(arr, left, middle - 1, x)
    else: 
        return -1

arr = [4,5,6,7,8,9,10]
x = 10

res = binary_search(arr,0,len(arr)-1,x)
if res != -1:
    print('Item found at: ' + str(res + 1))
else:
    print('Item not found')