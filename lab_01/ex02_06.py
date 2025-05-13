# Nhập X, Y
input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]  # Cách bằng dấu phẩy

rowNum = dimensions[0]
colNum = dimensions[1]

# Tạo ma trận
multilist = [[8 for col in range(colNum)] for row in range(rowNum)]

# In ma trận
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col
print(multilist)        

