def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        index = i
        value = arr[i]
        while index > 0 and arr[index - 1] > arr[index]:
            temp = arr[index- 1]
            arr[index - 1] = arr[index]
            arr[index] = temp
            index = index -1
        arr[index] = value

insertion_sort([3, 4, 56, 43, 2, 65, -1, -1, 56, 43])