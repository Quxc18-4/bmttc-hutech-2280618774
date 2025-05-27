class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        seen = set()
        matrix = []
        for char in key:
            if char.isalpha() and char not in seen:
                seen.add(char)
                matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                matrix.append(char)
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
        return None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.upper().replace("J", "I")
        plain_text = ''.join(filter(str.isalpha, plain_text))

        pairs = []
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            b = ''
            if i + 1 < len(plain_text):
                b = plain_text[i + 1]
            if a == b or b == '':
                b = 'X'
                i += 1
            else:
                i += 2
            pairs.append((a, b))

        encrypted_text = ""
        for a, b in pairs:
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # Loại bỏ 'X' cuối cùng nếu là padding
        if decrypted_text.endswith('X'):
            decrypted_text = decrypted_text[:-1]

        return decrypted_text
