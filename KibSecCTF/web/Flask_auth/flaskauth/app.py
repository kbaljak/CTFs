from flask import Flask, request, jsonify, session
import random
import string
from config import ADMIN_USERNAME, PW
import hashlib
import os
import string

app = Flask(__name__)

secret_key = hashlib.sha256(''.join(random.choices(
    string.digits, k=len("PW"))).encode("utf-8")).hexdigest()
app.secret_key = secret_key
print(app.secret_key)

users = {
    ADMIN_USERNAME: PW
}


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if PW == password:
        session['authenticated'] = True
        session['username'] = username
        print(session)
        return jsonify({"message": "Login successful"})
    print(session)
    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/flag')
def get_flag():
    app.logger.error("sess:" + str(session))
    if not session.get('authenticated'):
        return jsonify({"message": "Authentication required"}), 401

    return jsonify({
        "flag": os.environ.get("FLAG")
    })


if __name__ == '__main__':
    print(f"Generated secret key: {secret_key}")
    app.run(host='0.0.0.0', debug=True)
