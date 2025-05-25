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

#Remove Duplicates from a List Without Using Set
#Write a program to remove duplicate elements from a list without using the set() function.

original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = []
i = 0
while i < len(original_list):
    item = original_list[i]
    if item not in unique_list:
        unique_list.append(item)
    i += 1

print("List without duplicates:", unique_list)

def print_primes_upto_n(n):
    num = 2
    while num <= n:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num, end=' ')
        num += 1
    print()

# Example usage:
print("Prime numbers up to 30:")
print_primes_upto_n(30)