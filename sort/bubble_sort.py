def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0 , -1):
        v1 = arr[i]
        for j in range(i):
            v2 = arr[j + 1]
            if v1 >= v2:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)

bubble_sort([1, 7, 4, 3, -1])