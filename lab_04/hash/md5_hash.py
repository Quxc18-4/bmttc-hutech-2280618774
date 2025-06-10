import math

# Hàm quay trái 32-bit
def left_rotate(x, shift):
    return ((x << shift) | (x >> (32 - shift))) & 0xFFFFFFFF

# Bảng T[i] chuẩn của MD5
T = [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

# Hàm băm MD5
def md5(message):
    # Khởi tạo 4 biến A, B, C, D
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Bước tiền xử lý: padding
    original_length = len(message) * 8
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, byteorder='little')

    # Xử lý từng block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i + 64]
        M = [int.from_bytes(block[j:j + 4], byteorder='little') for j in range(0, 64, 4)]

        A, B, C, D = a, b, c, d

        for i in range(64):
            if i < 16:
                f = (B & C) | ((~B) & D)
                g = i
                s = [7, 12, 17, 22][i % 4]
            elif i < 32:
                f = (D & B) | ((~D) & C)
                g = (5 * i + 1) % 16
                s = [5, 9, 14, 20][i % 4]
            elif i < 48:
                f = B ^ C ^ D
                g = (3 * i + 5) % 16
                s = [4, 11, 16, 23][i % 4]
            else:
                f = C ^ (B | ~D)
                g = (7 * i) % 16
                s = [6, 10, 15, 21][i % 4]

            temp = D
            D = C
            C = B
            B = (B + left_rotate((A + f + T[i] + M[g]) & 0xFFFFFFFF, s)) & 0xFFFFFFFF
            A = temp

        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF

    # Nối kết quả thành chuỗi hexa theo thứ tự little-endian
    result = b''.join(x.to_bytes(4, byteorder='little') for x in [a, b, c, d])
    return result.hex()

# Chạy hàm băm từ input người dùng
if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")
    hash_value = md5(input_string.encode('utf-8'))
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {hash_value}")
