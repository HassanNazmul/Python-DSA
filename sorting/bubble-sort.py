# Bubble Sort
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