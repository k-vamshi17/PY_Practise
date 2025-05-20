# Merge & Sort Two Lists without using sorted()

# Define the first list
list1 = [5, 2, 9, 1]
# Define the second list
list2 = [8, 3, 7, 4]

# Merge the two lists into one
merged_list = list1 + list2

# Sort the merged list using bubble sort algorithm
# Outer loop for each element in the list
for i in range(len(merged_list)):
    # Inner loop to compare adjacent elements
    for j in range(0, len(merged_list) - i - 1):
        # Swap if the element found is greater than the next element
        if merged_list[j] > merged_list[j + 1]:
            merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

# Print the sorted merged list
print("Sorted List:", merged_list)
