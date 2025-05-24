from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
from flask import Flask
from fortune import get_fortune

chal = Flask(__name__)

KEY = ?

@chal.route('/fortune/get_fortune/<cookie>/<iv>/')
def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted_cookie = cipher.decrypt(cookie)
        unpadded_cookie = unpad(decrypted_cookie, 16)
    except ValueError as e:
        return {"error": str(e)}

    # magic function, i'm not allowed to show how it works
    return get_fortune(unpadded_cookie)


@chal.route('/fortune/get_cookie/')
def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"user=guest;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}

if __name__ == "__main__":
    print("Starting Flask app...")
    chal.run(debug=True, host="0.0.0.0", port=5000)
