'''write a python code without range
1
1 2 
1 2 3
1 2 3 4 '''

row = int(input("Value:"))
i=1
while i<=row:
    j=1
    while j<=i:
        print(j, end=' ')
        j +=1
    print()
    i +=1

## Count how many vowels (a, e, i, o, u) exist in a given string (case-insensitive).
lst=['a','e','i','o','u']
lst1=[]
word=list(input("Vowels :"))
for i in lst:
    if i in word:
        lst1.append(i)
print(len(lst1))

# Sort a List Without sort()
def sort_list(lst):
    n = len(lst)
    i = 0
    while i < n:
        j = 0
        while j < (n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1
    return lst

numbers = [0,5,2]
print("sorted list ",sort_list(numbers))

#3. Find the Second-Largest Number
def sort_list(lst):
    n = len(lst)
    i = 0
    while i < n:
        j = 0
        while j < (n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1
    return lst

numbers = [0,5,2]
sorted=sort_list(numbers)
print("second largest",sorted[-2])
