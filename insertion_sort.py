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