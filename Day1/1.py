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