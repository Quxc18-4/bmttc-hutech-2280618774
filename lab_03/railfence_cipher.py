import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_RailFence  # file UI bạn đã có


class RailFenceCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RailFence()
        self.ui.setupUi(self)

        # Kết nối nút
        self.ui.encrypt_btn.clicked.connect(self.encrypt)
        self.ui.decrypt_btn.clicked.connect(self.decrypt)

    def rail_fence_encrypt(self, plain_text, key):
        try:
            key = int(key)
            if key <= 0:
                raise ValueError
        except:
            self.show_error("Key phải là số nguyên dương.")
            return ""

        if key == 1:
            return plain_text

        rails = ['' for _ in range(key)]
        row = 0
        direction = 1
        for char in plain_text:
            rails[row] += char
            row += direction
            if row == 0 or row == key - 1:
                direction *= -1

        return ''.join(rails)

    def rail_fence_decrypt(self, cipher_text, key):
        try:
            key = int(key)
            if key <= 0:
                raise ValueError
        except:
            self.show_error("Key phải là số nguyên dương.")
            return ""

        if key == 1:
            return cipher_text

        n = len(cipher_text)
        fence = [[None] * n for _ in range(key)]

        row = 0
        direction = 1
        for i in range(n):
            fence[row][i] = True
            row += direction
            if row == 0 or row == key - 1:
                direction *= -1

        index = 0
        for r in range(key):
            for c in range(n):
                if fence[r][c] == True:
                    fence[r][c] = cipher_text[index]
                    index += 1

        result = []
        row = 0
        direction = 1
        for i in range(n):
            result.append(fence[row][i])
            row += direction
            if row == 0 or row == key - 1:
                direction *= -1

        return ''.join(result)

    def encrypt(self):
        plain_text = self.ui.plaintext_txt.toPlainText()
        key = self.ui.key_txt.toPlainText()
        if not plain_text:
            self.show_error("Bạn chưa nhập Plain text.")
            return
        if not key:
            self.show_error("Bạn chưa nhập Key.")
            return
        encrypted_text = self.rail_fence_encrypt(plain_text, key)
        self.ui.ciphertext_txt.setPlainText(encrypted_text)
        self.show_info("Mã hóa thành công.")

    def decrypt(self):
        cipher_text = self.ui.ciphertext_txt.toPlainText()
        key = self.ui.key_txt.toPlainText()
        if not cipher_text:
            self.show_error("Bạn chưa nhập Cipher text.")
            return
        if not key:
            self.show_error("Bạn chưa nhập Key.")
            return
        decrypted_text = self.rail_fence_decrypt(cipher_text, key)
        self.ui.plaintext_txt.setPlainText(decrypted_text)
        self.show_info("Giải mã thành công.")

    def show_error(self, msg):
        dlg = QMessageBox(self)
        dlg.setIcon(QMessageBox.Critical)
        dlg.setWindowTitle("Lỗi")
        dlg.setText(msg)
        dlg.exec_()

    def show_info(self, msg):
        dlg = QMessageBox(self)
        dlg.setIcon(QMessageBox.Information)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(msg)
        dlg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RailFenceCipherApp()
    window.show()
    sys.exit(app.exec_())
