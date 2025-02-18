# Selection Sort Algorithm

"""
Selection Sort Algorithm

Selection Sort is a simple, comparison-based sorting algorithm that repeatedly
selects the smallest element from the unsorted portion of the list and places
it in its correct position. It maintains two sublists: one sorted and one
unsorted.

How It Works:
-------------
1. Find the smallest element in the unsorted sublist.
2. Swap it with the leftmost unsorted element.
3. Expand the sorted sublist by moving the boundary one step to the right.
4. Repeat until the entire list is sorted.

Time Complexity:
----------------
- Worst Case: O(n²) (when the list is in reverse order)
- Best Case: O(n²) (Selection Sort always performs O(n²) comparisons)
- Average Case: O(n²)

Space Complexity:
-----------------
- O(1) (since Selection Sort is an in-place sorting algorithm)

Stable Sort?:
-------------
- No, Selection Sort is not stable because swapping can change the relative
  order of equal elements.

"""

def selection_sort(arr):
    arr_size = len(arr) # Get the size of the array

    # Perform Selection Sort
    for i in range(arr_size): # Loop through the array until the size of the array
        min_index = i # Set the minimum index to the current index
        for j in range(i + 1, arr_size): # Loop through the array from the next index to the size of the array
            if arr[j] < arr[min_index]: # If the current element is less than the minimum element then update the minimum index
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i] # Swap the current element with the minimum element


# Test the Function
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)

    selection_sort(arr)
    print("Sorted Array:", arr)