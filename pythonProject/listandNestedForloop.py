

nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10]
]

print(nested_list)
print('##############################')
for row in nested_list:
    print(row)

print('######################')

for row in nested_list:
    for col in row:
        print(col)