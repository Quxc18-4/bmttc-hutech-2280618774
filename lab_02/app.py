from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Trang chủ
@app.route("/")
def home():
    return render_template("index.html")

# ====== Caesar Cipher ======
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        text = request.form["inputPlainText"]
        key = int(request.form["inputKeyPlain"])
        caesar = CaesarCipher()
        encrypted = caesar.encrypt_text(text, key)
        return jsonify(success=True, message=f"Kết quả mã hóa: {encrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        text = request.form["inputCipherText"]
        key = int(request.form["inputKeyCipher"])
        caesar = CaesarCipher()
        decrypted = caesar.decrypt_text(text, key)
        return jsonify(success=True, message=f"Kết quả giải mã: {decrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))


# ====== Vigenère Cipher ======
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        text = request.form["inputPlainText"]
        key = request.form["inputKeyPlain"]
        vigenere = VigenereCipher()
        encrypted = vigenere.vigenere_encrypt(text, key)
        return jsonify(success=True, message=f"Kết quả mã hóa: {encrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        text = request.form["inputCipherText"]
        key = request.form["inputKeyCipher"]
        vigenere = VigenereCipher()
        decrypted = vigenere.vigenere_decrypt(text, key)
        return jsonify(success=True, message=f"Kết quả giải mã: {decrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))


# ====== Rail Fence Cipher ======
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        text = request.form["inputPlainText"]
        key = int(request.form["inputKeyPlain"])
        railfence = RailFenceCipher()
        encrypted = railfence.rail_fence_encrypt(text, key)
        return jsonify(success=True, message=f"Kết quả mã hóa: {encrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        text = request.form["inputCipherText"]
        key = int(request.form["inputKeyCipher"])
        railfence = RailFenceCipher()
        decrypted = railfence.rail_fence_decrypt(text, key)
        return jsonify(success=True, message=f"Kết quả giải mã: {decrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))


# ====== Playfair Cipher ======
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt_route():
    try:
        text = request.form["inputPlainText"]
        key = request.form["inputKeyPlain"]
        playfair = PlayFairCipher()
        matrix = playfair.create_playfair_matrix(key)  # Tạo ma trận 5x5 từ key
        encrypted = playfair.playfair_encrypt(text, matrix)  # Truyền ma trận chứ không phải key
        return jsonify(success=True, message=f"Kết quả mã hóa: {encrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt_route():
    try:
        text = request.form["inputCipherText"]
        key = request.form["inputKeyCipher"]
        playfair = PlayFairCipher()
        matrix = playfair.create_playfair_matrix(key)
        decrypted = playfair.playfair_decrypt(text, matrix)
        return jsonify(success=True, message=f"Kết quả giải mã: {decrypted}")
    except Exception as e:
        return jsonify(success=False, message=str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
