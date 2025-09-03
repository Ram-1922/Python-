#nested loops
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

rows=int(input("Enter no of rows:"))
column=int(input("Enter no columns:"))
symbol=input("Enter the item:")
for i in range(rows):
    for j in range(column):
        print(symbol, end=' ')
    print()