# Bubble Sort Algorithm

"""
Bubble Sort Algorithm

Bubble Sort is a simple, comparison-based sorting algorithm that repeatedly
swaps adjacent elements if they are in the wrong order. This process continues
until the entire list is sorted.

How It Works:
-------------
1. Start at the first element and compare it with the next element.
2. Swap them if they are in the wrong order.
3. Move to the next adjacent pair and repeat this process for the entire list.
4. After each full pass, the largest unsorted element is placed at its correct position.
5. Repeat this process until no swaps are needed, meaning the list is sorted.

Time Complexity:
----------------
- Worst Case: O(n²) (when the list is in reverse order)
- Best Case: O(n) (when the list is already sorted)
- Average Case: O(n²)

Space Complexity:
-----------------
- O(1) (since Bubble Sort is an in-place sorting algorithm)

"""

def bubble_sort(elements):
    elements_size = len(elements) # Get the size of the elements

    # Perform Bubble Sort
    for i in range(elements_size): # Loop through the elements until the size of the elements
        for j in range(0, elements_size - 1 - i): # Loop through the elements until the size of the elements - i - 1
            if elements[j] > elements[j + 1]: # If the current element is greater than the next element then swap the elements
                temp = elements[j] # Store the current element in a temporary variable
                elements[j] = elements[j + 1] # Swap the current element with the next element
                elements[j + 1] = temp # Swap the next element with the current element


    # Perform Bubble Sort (Optimized)
    for i in range(elements_size): # Loop through the elements until the size of the elements
        swapped = False # Set swapped to False
        for j in range(0, elements_size - 1 - i): # Loop through the elements until the size of the elements - i - 1
            if elements[j] > elements[j + 1]: # If the current element is greater than the next element then swap the elements
                elements[j], elements[j + 1] = elements[j + 1], elements[j] # Swap the current element with the next element
                swapped = True # Set swapped to True
        if not swapped: # If swapped is False then break the loop
            break


# Test the Function
if __name__ == "__main__":
    elements = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort(elements)
    print(elements)