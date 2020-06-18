matrix1 = []
matrix2 = []
matrix3 = []

n = int(input())

for i in range(0, n):
    row = []
    rowString = input()
    rowString = rowString.split(" ")
    for j in range(0, n):
        rowInt = int(rowString[j])
        row.append(rowInt)
    matrix1.append(row)

x = input()

for i in range(0, n):
    row = []
    rowString = input()
    rowString = rowString.split(" ")
    for j in range(0, n):
        rowInt = int(rowString[j])
        row.append(rowInt)
    matrix2.append(row)

for i in range(0, n):
    row = []
    for j in range(0, n):
        elem = 0
        row.append(elem)
        print(elem)
    matrix3.append(row)

print(matrix3)

