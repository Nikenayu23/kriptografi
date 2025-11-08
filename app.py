from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate key untuk enkripsi (biasanya disimpan aman)
key = Fernet.generate_key()
cipher = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    text = request.form['plaintext']
    encrypted = cipher.encrypt(text.encode()).decode()
    return render_template('index.html', encrypted_text=encrypted)

@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    text = request.form['ciphertext']
    decrypted = cipher.decrypt(text.encode()).decode()
    return render_template('index.html', decrypted_text=decrypted)

if __name__ == '__main__':
    app.run(debug=True)
