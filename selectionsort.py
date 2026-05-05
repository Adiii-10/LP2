def SelectionSort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_ind = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        
        # swap
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()


if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    
    arr = []
    print("Enter the elements:")
    for i in range(n):
        arr.append(int(input()))
    
    SelectionSort(arr)
    
    print("Sorted array:")
    print_array(arr)
