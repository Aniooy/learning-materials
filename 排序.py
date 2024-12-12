'''
(0) [46 74 53 14 26 38 86 65 27 34]
(1) [46 53 14 26 38 74 65 27 34] 86
(2) [46 14 26 38 53 65 27 34] 74 86
(3) [14 26 38 46 53 27 34] 65 74 86
(4) [14 26 38 46 27 34] 53 65 74 86
(5) [14 26 38 27 34] 46 53 65 74 86
(6) [14 26 27 34] 38 46 53 65 74 86
(7) [14 26 27 34] 38 46 53 65 74 86
'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iteration {i + 1}: {arr}")


# Test the function
arr = [46, 74, 53, 14, 26, 38, 86, 65, 27, 34]
bubble_sort(arr)

a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, -7744, 144, 182, 196, 12, -16, -49, 15129, 441, 484, 529, 576)
print(sum(a))
