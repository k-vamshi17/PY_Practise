# 1. Merge & Sort Two Lists without using sorted()

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

# 2.Inverted Number Pyramid
# 📌 Problem: Print this pattern without range() or string multiplication:
n = 5 # You can change the height as needed 

row = n
while row > 0:
    num = 1
    count = 0
    line = []
    while count < row:
        line.append(str(num))
        num += 1
        count += 1
    print(' '.join(line))
    row -= 1 