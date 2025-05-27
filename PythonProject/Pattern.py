x = 4
for i in range (1, x+1):
    for j in range (1 , i+1):
        print("*" , end="")
    print()

Row = 5
for i in range(Row):
    for j in range (0,i):
        print(i,end="")
    print()

Row = 6
for i in range(Row):
    for j in range(i,Row-1):
        print(i,end="")
    print()


list = [2,56,9,8,4,456,45,48,4,8564,6]

largest_number = None

for i in (list):
    if largest_number ==  None or largest_number < i :
        largest_number = i
print(largest_number)