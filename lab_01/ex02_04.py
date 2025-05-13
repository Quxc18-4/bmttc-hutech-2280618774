#tạo danh sách trống j
j = []
#duyệt các số từ range 2000-3200 mà chia hết cho 7
for i in range (2000,3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))

print(','.join(j))
        