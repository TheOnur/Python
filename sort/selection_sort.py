def selection_sort(arr):
    n = len(arr)
    for index in range(n):
        def min_index(index, arr):
            min_index = index
            for i in range(index + 1, len(arr)):
                if arr[i] < arr[min_index]:
                    min_index = i
            return min_index
        minimum = min_index(index, arr)
        def swap(minimum, index, arr):
            temp = arr[minimum]
            arr[minimum] = arr[index]
            arr[index] = temp
        swap(minimum, index, arr)
    print(arr)

selection_sort([565, 32, 2, 4, -1, 34, 232, 2])