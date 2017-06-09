def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1 , -1):
        def heapify(arr, i, n):
            """
               Heap is a specialized tree-based data structure. 
               At index i, 2 * i + 1 gives the left child and 2 * i + 2 gives the right child.
               After maximizing the heap, i.e, parent node can not be smaller than childs, replace the root with child lead and do the same operation recursively.  
            """
            index = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[i] < arr[left]:
                index = left
            
            if right < n and arr[index] < arr[right]:
                index = right

            if index != i:
                temp = arr[index]
                arr[index] = arr[i]
                arr[i] = temp
                heapify(arr, index, n)

    for i in range(n-1, 0, -1):
        def swap(arr, i):
            temp = arr[i]
            arr[i] = arr[0]
            arr[0] = temp
        swap(arr, i)
        heapify(arr, 0, i )
    print(arr)
    

heap_sort([3, 12, 44, 32, 1, -1])