def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    
    Args:
        arr (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def test_bubble_sort():
    """
    Test cases for the bubble_sort function.
    """
    # Test case 1: Sorting a simple list
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    
    # Test case 2: Sorting a list with negative numbers
    assert bubble_sort([-3, -1, -2, -4, -5]) == [-5, -4, -3, -2, -1]
    
    # Test case 3: Sorting an already sorted list
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 4: Sorting an empty list
    assert bubble_sort([]) == []
    
    # Test case 5: Sorting a list with duplicate elements
    assert bubble_sort([5, 3, 5, 3, 2]) == [2, 3, 3, 5, 5]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_bubble_sort()