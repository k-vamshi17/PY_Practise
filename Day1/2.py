# Count how many vowels (a, e, i, o, u) exist in a given string (case-insensitive).
lst=['a','e','i','o','u']
lst1=[]
word=list(input(":"))
for i in lst:
    if i in word:
        lst1.append(i)
print(len(lst1))