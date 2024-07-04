# Password encryption program

import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)

user_pass = input("Enter your password: ")
encrypt_pass(user_pass)

# Password decryption program

# import base64 - Add it if you haven't imported this library yet

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password: {decode_data}")

encode_string = input("Enter the base64 string: ")
decode_pass(encode_string)
