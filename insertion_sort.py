# Insertion Sort Algorithm

"""
Insertion Sort Algorithm

Insertion Sort is a simple, comparison-based sorting algorithm that builds the
final sorted list one element at a time by shifting elements instead of swapping.
It is more efficient than Bubble Sort and Selection Sort for nearly sorted data
but less efficient than advanced algorithms like Quick Sort and Merge Sort.

How It Works:
-------------
1. Start with the second element (key) and compare it with the first element.
2. If the key is smaller, shift the larger element to the right.
3. Continue moving left until the correct position for the key is found.
4. Insert the key into its correct position in the sorted sublist.
5. Repeat until the entire list is sorted.

Time Complexity:
----------------
- Worst Case: O(n²) (when the list is in reverse order)
- Best Case: O(n) (when the list is already sorted, as only comparisons are needed)
- Average Case: O(n²)

Space Complexity:
-----------------
- O(1) (since Insertion Sort sorts the list in place)

"""

def insertion_sort(arr):
    for i in range(1, len(arr)): # Loop through the array starting from the second element
        key = arr[i] # Get the current element
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]: # Loop through the sorted sublist
            arr[j + 1] = arr[j] # Shift the elements to the right
            j -= 1

        arr[j + 1] = key # Insert the key into its correct position


# Test the Function
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)

    insertion_sort(arr)
    print("Sorted Array:", arr)